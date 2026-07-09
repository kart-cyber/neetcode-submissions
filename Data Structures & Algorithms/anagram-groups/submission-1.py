class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            r[sortedS].append(s)
        return list(r.values())

            