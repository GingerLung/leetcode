# 題目:有一個由小排到大的list叫"nums"，請用O(log n)-->二元搜尋法的方式，回傳目標在"nums"的位置
# 若目標不在"nums"，回傳目標應該插入在哪一個位置
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        max = len(nums)-1 
        min = 0

        while min <= max: # 不指定次數，條件成立就會一直執行
            middle =(min+max)//2 # 確保middle為整數
            if target == nums[middle]: # 成功條件
                return middle

            elif target < nums[middle]: # 中間值比目標大，所以設定最大值為原中間值 - 1
                max = middle -1
            elif target > nums[middle]: # 中間值比目標大，所以設定最小值為原中間值 + 1
                min = middle +1
        else : # 如果目標不在"nums"，回傳上面迴圈最後的中間值，但是中間值寫在上面那個迴圈，這邊指定不到，只好指定最小值(最大值也可)
            return min # 這邊需要回傳最小值，因為"最大值小於最小值"，才跳出迴圈
            # return max +1 最大值加1才是我要的值


if __name__ == "__main__":

    nums = [1, 3, 5, 6]
    target = 5
    result = Solution().searchInsert(nums, target)

    print(result)  
