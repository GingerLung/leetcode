class Solution:
    def removeElement(self, nums, val):
        k = 0  # 用來記錄不等於 val 的元素數量
        for i in range(len(nums)):
            if nums[i] != val:  # 如果當前元素不等於 val
                nums[k] = nums[i]  # 將這個元素移到前面的 k 位置
                k += 1  # 更新 k，表示已經放置了一個新的不等於 val 的元素
        return k  # 返回不等於 val 的元素數量
        
