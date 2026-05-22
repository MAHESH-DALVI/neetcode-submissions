class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # If list is empty
        if not strs:
            return ""
        
        # Initialize prefix as the first string
        prefix = strs[0]

        # Compare prefix with all other strings
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                
                # If prefix becomes empty, no common prefix
                if prefix == "":
                    return ""
        
        # Final prefix after comparison
        return prefix
