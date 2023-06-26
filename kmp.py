def _build_next(needle: str) -> [int]:
    """
    next[i] 代表 needle[0:i] 中最长公共前后缀
    当 needle[i] 失配时 即在下一个位置回溯到 needle[next[i]] 重新开始匹配
    :param needle: str
    :return: next 数组
    """
    le = len(needle)

    nex = [0] * le

    j = 0
    t = nex[0] = -1

    while j < le - 1:
        if 0 > t or needle[j] == needle[t]:
            j += 1
            t += 1
            # t - 1 = next[j - 1]
            # i = next[j - 1] + 1
            # if needle[i] == needle[j] : next[j] = next[t] j 失配 也可以看成是在 t 失配
            # else next[j] = t  j 失配时回溯到 t
            if needle[j] != needle[t]:
                nex[j] = t
            else:
                nex[j] = nex[t]
        else:
            # i = next[j]
            # if needle[i] != needle[j] : i = next[i]
            t = nex[t]

    return nex


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        nex = _build_next(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] != needle[j] and j >= 0:
                j = nex[j]
            else:
                i += 1
                j += 1

        return i - j
