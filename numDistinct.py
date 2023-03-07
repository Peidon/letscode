class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dic = dict(zip([x for x in s], [0 for i in range(len(s))]))

        for ch in s:
            dic[ch] += 1

        k_list = [x for x in dic.keys()]

        for i in range(1, len(dic)):
            for j in range(i):
                two = k_list[j] + k_list[i]
                if two in dic:
                    dic[two] += 1
                else:
                    dic[two] = 1

        return self.countSeq(t, dic)

    def countSeq(self, t, dic, two=None):

        if len(t) == 1 or len(t) == 2:
            if two in dic:
                return dic[t]
            else:
                return 0
        return min(self.countSeq(t[1:], dic), self.countSeq(t[:-1], dic))


if __name__ == '__main__':
    ans = Solution().numDistinct("rabbbit", "rabbit")
    print(ans)
