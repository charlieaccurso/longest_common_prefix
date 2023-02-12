class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp= strs[0]

        # BASE CASE
        if len(strs) == 1:
            return lcp
        
        # RECURSIVE CASE
        for word in strs:
            if word == "":
                return ""
            if word[0] != lcp[0]:
                return ""
            max_iter= min(len(word), len(lcp))
            new_lcp= ""
            i= 0
            while i < max_iter and lcp[i] == word[i]:
                new_lcp+= lcp[i]
                i+= 1
            lcp= new_lcp
        return lcp
