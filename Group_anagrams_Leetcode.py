from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
            print(res)
        return list(res.values())
    

Y = Solution()
Y.groupAnagrams(["act","pots","tops","cat","stop","hat"])
        