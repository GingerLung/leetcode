"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""
# python 3.10.10 


# Example 1:
"""
Input: s = "()"
Output: true
"""
class Solution(object):
    def __init__(self, s: str) -> bool:
        # 構造函數接收輸入的字串並儲存
        self.str_ = s         
    
    def isValid(self):
        # 定義一個堆疊來儲存開括號
        stack = []
        print(type(stack))
        # 括號對應字典
        bracket_map = {')': '('
                       , '}': '{'
                       , ']': '['}
        
        # 遍歷每個字符
        for char in self.str_:
            # 如果是閉括號，檢查堆疊頂端是否有對應的開括號
            if char in bracket_map:
                # 若堆疊為空或頂端括號不匹配，返回 False
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # 如果是開括號，將其放入堆疊
                stack.append(char)
        
        # 如果堆疊最後是空的，則表示所有括號都有正確配對
        return not stack    
        

if __name__ == "__main__":
    while True:
        ob_cb = input(r"Input ()or{}or[]: ").strip()
        brks = Solution(ob_cb)
        print("Output : ", brks.isValid(),"\n")



# Example 2:
"""
Input: s = "()[]{}"
Output: true
"""


# Example 3:
"""
Input: s = "(]"
Output: false
"""

# Example 4:
"""
Input: s = "([])"
Output: true
"""

 
# ---------------------------------------------- #
"""
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


##########
# Frank. #
##########