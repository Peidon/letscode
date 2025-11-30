from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        new_st = newInterval[0]
        new_ed = newInterval[1]
        i = 0
        while i < len(intervals) and intervals[i][1] < new_st:
            merged.append(intervals[i])
            i+=1

        if i < len(intervals):
            new_st = min(new_st, intervals[i][0])

        while i < len(intervals) and intervals[i][0] <= new_ed:
            i+=1

        if i-1 >= 0:
            new_ed = max(intervals[i-1][1],new_ed)

        merged.append([new_st, new_ed])
        while i < len(intervals):
            merged.append(intervals[i])
            i+=1
        return merged


if __name__ == '__main__':
    a = [[1,5]]
    b = [0,0]
    c = Solution().insert(a, b)

    print(c)