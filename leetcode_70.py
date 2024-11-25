# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# 時間會超過
class solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        elif n == 2 :
            return 2
        elif n > 2:
            return solution().climbStairs(n-1) + solution().climbStairs(n-2)    
print(solution().climbStairs(37))


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        # 初始化dp陣列
        dp = [0] * (n + 1)
        dp[0] = 1  # 基本情況：地面
        dp[1] = 1  # 基本情況：第一階

        # 從 n-1 階爬一階，也可以從 n-2 階爬兩階
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

print(Solution().climbStairs(37))  # 這裡會輸出到達第5階的不同方式數
