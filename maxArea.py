class Solution():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, volume = 0, len(height) - 1, 0
        while(left < right):
            if(height[left] > height[right]):
                volume = max((right - left) * height[right], volume)
                while(right > left and height[right - 1] <= height[right]):
                    right -= 1
                right -= 1
            else:
                volume = max((right - left) * height[left], volume)
                while(right > left and height[left + 1] <= height[left]):
                    left += 1
                left += 1
        return volume

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))