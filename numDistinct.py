class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        for ch in s: dic[ch] += 1
        kelist = dic.keys()
        for i in range(1, len(dic)):
            for j in range(i):
                two = kelist[j] + kelist[i]
                dic[two] += 1

        return self.countSeq(t, dic)

    def countSeq(self, t, dic, two=None):

        if len(t) == 1 or len(t) == 2:
            if dic[two]:
                return dic[t]
            else:
                return 0
        return min(self.countSeq(t[1:], dic), self.countSeq(t[:-1], dic))


ans = Solution().numDistinct("rabbbit", "rabbit")
print(ans)