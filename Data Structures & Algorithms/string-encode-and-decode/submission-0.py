class Solution: 
    def encode(self, strs: list[str]) -> str:
        encoded_list = []
        for word in strs:
            chunk = str(len(word)) + "#" + word 
            encoded_list.append(chunk)
            
        # Pushed out to the left! Wait until the 'for' loop is done.
        return "".join(encoded_list)

    def decode(self, s: str) -> list[str]:
        decoded_strs = []
        i = 0
        
        while i < len(s):
            j = i
            
            # This loop's ONLY job is to find the '#'
            while s[j] != '#':
                j += 1
                
            # These lines are pushed back to the left!
            # We only do this AFTER j has found the '#'
            word_length = int(s[i:j])
            word = s[j + 1 : j + 1 + word_length]
            decoded_strs.append(word)
            
            # Move 'i' to the next word chunk
            i = j + 1 + word_length 
            
        return decoded_strs