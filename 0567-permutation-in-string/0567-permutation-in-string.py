class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_s = [0]*26
        hash_w = [0]*26
        window_length = len(s1)

        def is_hash_same(h1, h2):
            return h1 == h2

        for i in range(window_length):
            hash_s[ord(s1[i])-ord('a')]+=1
            hash_w[ord(s2[i])-ord('a')]+=1

        i=0
        j=window_length-1
        while j<len(s2):
            if is_hash_same(hash_s, hash_w):
                return True
            hash_w[ord(s2[i])-ord('a')]-=1
            i+=1
            j+=1
            if j<len(s2):
                hash_w[ord(s2[j])-ord('a')]+=1
        return False