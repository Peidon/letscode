import unittest
from typing import List

'''
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

def productExceptSelf(nums: List[int]) -> List[int]:
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


class Test0(unittest.TestCase):

    def test_product(self):
        d = [0,2,0,4]
        o = productExceptSelf(d)
        expect = [0, 0, 0, 0]
        self.assertEqual(o, expect, msg="example #1")



if __name__ == '__main__':
    Test0().test_product()