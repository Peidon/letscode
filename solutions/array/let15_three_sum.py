from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
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