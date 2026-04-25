class Codec:
    # Date Solved: 25 April 2026, Saturday
    # Refer: NeetCode Blind 75 and NeetCode 150 Course on freeCodeCamp.org
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string using
        the format: <length>#<string>
        """
        encoded_str = ""
        for s in strs:
            # Prepend the length and a delimiter '#'
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """
        Decodes the single string back into the original list.
        """
        decoded_strings, i = [], 0
        while i < len(s):
            # Find the delimiter to determine where the length number ends
            j = i
            while s[j] != "#":
                j += 1
            # Extract the length and the actual string content
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_strings.append(word)
            # Move index to the start of the next encoded segment
            i = j + 1 + length
        return decoded_strings


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
