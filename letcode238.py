from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products, reverse, lis = [nums[0]], [nums[-1]], []
        n = len(nums)
        for num in nums[1:n-1]:
            products.append(products[-1] * num)
        for i in range(n - 2, 0, -1):
            reverse.append(reverse[-1] * nums[i])

        for i in range(len(nums)):
            if 0 < i < n - 1:
                lis.append(products[i-1] * reverse[n - i - 2])
            if i == 0:
                lis.append(reverse[-1])
            if i == n - 1:
                lis.append(products[-1])

        return lis

if __name__ == '__main__':
    a = [0,2,0,4]
    b = Solution().productExceptSelf(a)
    print(b)