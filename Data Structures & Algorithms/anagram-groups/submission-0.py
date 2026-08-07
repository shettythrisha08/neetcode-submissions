class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for item in strs:
            sitem="".join(sorted(item))
            if sitem in groups:
                groups[sitem].append(item)
            else:
                groups[sitem]=[item]
        return list(groups.values())