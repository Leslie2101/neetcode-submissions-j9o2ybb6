class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            canonicalChars = sorted(string)
            canonicalStr = "".join(canonicalChars)
            groups[canonicalStr].append(string)
        
        return list(groups.values())