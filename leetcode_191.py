# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
# 給一正整數，回傳二進位制數字的各項數字和 ex : 5 -> 101 -> 2

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_n = bin(n)
        sum = 0
        for num in range(len(str(binary_n))):
            if  binary_n[num] == "1":
                sum += 1
        return sum        


print(Solution().hammingWeight(5))

