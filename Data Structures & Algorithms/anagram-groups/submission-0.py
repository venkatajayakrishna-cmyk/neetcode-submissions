class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            d[key].append(str)
        return list(d.values())