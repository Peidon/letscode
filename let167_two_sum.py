from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers)-1
        while small < big:
            a = numbers[small]
            b = numbers[big]
            if target == a + b:
                return [small+1, big+1]
            if target > a + b:
                small += 1
            else:
                big -= 1

        return [small+1, big+1]

if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    lis = Solution().twoSum(numbers, target)
    print(lis)