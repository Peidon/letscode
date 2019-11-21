class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.minHeap(nums, k)
        for i in range(k, len(nums)):
            if nums[i] > nums[0]:
                nums[0] = nums[i]
                self.minHeap(nums, k)
        return nums[0]

    def minHeap(self, nums, k):
        bottom = k // 2 - 1

        while bottom >= 0:
            down = bottom
            t = nums[bottom]

            while down * 2 + 1 < k:
                tmin = down * 2 + 1
                rt = (down + 1) * 2
                if rt < k and nums[tmin] > nums[rt]:
                    tmin = rt
                if nums[tmin] < nums[down]:
                    nums[down] = nums[tmin]
                    down = tmin
                else: break
            nums[down] = t

            bottom -= 1
            
    def findKthLargest_(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            p = self.pivot(nums, start, end)
            if p > k - 1: end = p - 1
            elif p < k - 1: start = p + 1
            else: break
        return nums[k - 1]


    def pivot(self, nums, start, end):
        tmp =  nums[start]
        while start < end:
            while start < end and tmp >= nums[end]: end -= 1
            nums[start] = nums[end]
            while start < end and nums[start] >= tmp: start += 1
            nums[end] = nums[start]
        nums[start] = tmp
        return start
        
ans = Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 3)
print(ans)