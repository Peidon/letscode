def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    intervals.sort(key=lambda x: x[0])

    offset = 0
    for a, b in intervals[1:]:
        if intervals[offset][-1] >= a:
            intervals[offset][-1] = max(b, intervals[offset][-1])
        else:
            # intervals[i] of intervals[1:], equals intervals[i-1] of intervals
            # intervals[offset][-1] = max(intervals[i][-1], intervals[offset][-1])
            offset+=1
            intervals[offset] = [a, b]

    return intervals[:offset+1]


if __name__ == '__main__':
    m = merge([[1,3],[2,6],[8,10],[15,18]])
    print(m)