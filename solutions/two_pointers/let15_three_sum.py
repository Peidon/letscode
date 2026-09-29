from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    the useful strategy is to shrink the scope of the problem step by step.
    step 1, make the list ordered, this is very important,
    that allows us to find out the solutions alongside the iteration.
    assuming there are already three nums are satisfied the requirement.
    They may be 2 nums < 0, 1 number > 0, or 2 nums > 0, 1 number < 0.
    Or we can say , at least one number > 0, one number < 0.
    So, the scope is definite.
    When the nums is sorted, left one is the minimum, and right one is the maximum,

    """
    nums.sort()
    lis = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            x, y, z = nums[i], nums[j], nums[k]
            if x + y + z == 0:
                lis.append([x, y, z])
                k -= 1
                j += 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
                while j < k and nums[k + 1] == nums[k]:
                    k -= 1

            elif x + y + z > 0:
                k -= 1
            else:
                j += 1
    return lis

if __name__ == '__main__':
    a = [0,0,0,0,0,0,0]
    b = threeSum(a)
    print(b)