"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
# python 3.10.10 


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return r'""'
    
        # 假設最長公共前綴是第一個字串
        prefix = strs[0]
        
        # 比較每個字串與當前的最長公共前綴
        for s in strs[1:]:
            # 將 prefix 縮小至與當前字串的公共部分
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # 去掉最後一個字元
                if not prefix:
                    return r'""'  # 如果公共前綴變空，則返回空字串
        
        return prefix
    

if __name__=="__main__":
    solution = Solution()

    # Example 1:
    strs = ["flower","flow","flight"]
    # Output: "fl"
    print(solution.longestCommonPrefix(strs))

    # Example 2:
    strs = ["dog","racecar","car"]
    # Output: ""
    print(solution.longestCommonPrefix(strs))

"""
startswith() 是 Python 字串（str）類型的一個內建方法，
它用來檢查字串是否以指定的子字串開頭。這個方法返回一個布林值 True 或 False，表示字串是否符合條件。
"""
# ## True
# strs = ["flower","flow","flight"]
# s = "flow" # strs[1]
# prefix = "flower" # strs[0]
# print(not s.startswith(prefix))

# ## False
# strs = ["flower","flow","flight"]
# s = "flow" # strs[1]
# prefix = "flo" # strs[0]
# print(not s.startswith(prefix))


##########
# Frank. #
##########