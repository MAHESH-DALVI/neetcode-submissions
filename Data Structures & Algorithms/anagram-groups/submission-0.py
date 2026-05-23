class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cubby_shelf = {}
        
        for word in strs: 
            name_tag = "".join(sorted(word))
            
            if name_tag not in cubby_shelf:
                cubby_shelf[name_tag] = []
                
            cubby_shelf[name_tag].append(word)
            
        # Notice how this line is pushed out to the left!
        return list(cubby_shelf.values())