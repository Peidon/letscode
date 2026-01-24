def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    merged = []
    intervals.sort(key=lambda x: x[0])

    if len(intervals) > 0:
        merged.append(intervals[0])
    for interval in intervals:
        if merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])

    return merged


class Solution(object):
    pass
