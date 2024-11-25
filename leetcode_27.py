class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        while val in nums:
            nums.remove(val)
            count +=1
        return len(nums)-count    


        