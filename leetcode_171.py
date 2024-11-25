# Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = list(columnTitle)[::-1] # AB -> 26+2 反轉後BA -> 2+26
        
        number = 0
        for i in range(len(alpha)):
            num = ord(alpha[i]) - 64    # ord(A)->65 ; ord(Z)->90
            number += num * (26**i)     # list[0]*26的0次方，list[1]*26的1次方
        
        return number


# print(Solution().titleToNumber("AHSSHS"))
