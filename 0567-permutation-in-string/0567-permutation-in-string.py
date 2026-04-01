class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_s1 = [0]*26
        hash_window = [0]*26
        window_length = len(s1)

        def is_hash_same(h1, h2):
            return h1 == h2

        for i in range(window_length):
            hash_s1[ord(s1[i])-ord('a')]+=1
            hash_window[ord(s2[i])-ord('a')]+=1

        i=0
        j=window_length-1
        while j<len(s2):
            if is_hash_same(hash_s1, hash_window):
                return True
            hash_window[ord(s2[i])-ord('a')]-=1 #if hash not matched then revert hash_window to all 0
            i+=1
            j+=1
            if j<len(s2):
                hash_window[ord(s2[j])-ord('a')]+=1 #update window hash with next set of characters
        return False