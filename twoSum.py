from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}

    for i, num in enumerate(nums):
        if target - num in dic:
            return [dic.get(target - num), i]
        dic[num] = i

    return []
