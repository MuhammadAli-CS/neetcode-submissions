class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for item in strs:
            sgrp="".join(sorted(item))
            if sgrp in groups:
                groups[sgrp].append(item)
            else: groups[sgrp]= [item]

        return list(groups.values())