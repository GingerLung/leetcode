# O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        times = len(nums) 
        i=0
        nums_copy = nums.copy()
        while i < times :
            for k in range(times-1, i, -1):
                if nums[i] + nums_copy[k] == target : 
                    return [i, k]
            i += 1