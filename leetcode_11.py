# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# 給定一個長度為 n 的整數數組。繪製 n 條垂直線，第 i 條線的兩個端點為 (i, 0) 和 (i, height[i])。
# 求與 x 軸一起形成容器的兩條線，使得該容器包含最多的水。
# 返回容器可以儲存的最大水量。
# 請注意，你不能傾斜容器。

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        volumes = []
        while left < right:
            volume = (right - left) * min(height[left], height[right])
            volumes.append(volume)
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -=1
        return max(volumes)


# def max_area(height):
#     """
#     計算最大容器可以儲存的水量
#     :param height: List[int] - 每條線的高度
#     :return: int - 最大水量
#     """
#     left, right = 0, len(height) - 1  # 初始化雙指針
#     max_water = 0  # 儲存最大水量

#     while left < right:
#         # 計算當前容器的水量
#         width = right - left
#         current_water = min(height[left], height[right]) * width
#         max_water = max(max_water, current_water)  # 更新最大水量

#         # 移動指針
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1

#     return max_water

# # 測試範例
# heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(max_area(heights))  # 輸出應為 49
        
