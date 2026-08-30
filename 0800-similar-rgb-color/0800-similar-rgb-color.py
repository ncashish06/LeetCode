class Solution:
    # Date Solved: 30 August 2026, Sunday, Weekly Premium W5
    # Refer: Claude
    def similarRGB(self, color: str) -> str:
        def closest(hexPair: str) -> str:
            val = int(hexPair, 16)
            best_digit = 0
            best_diff = float("inf")
            for d in range(16):
                candidate = d * 17  # e.g. 0x11 * d
                diff = (candidate - val) ** 2
                if diff < best_diff:
                    best_diff = diff
                    best_digit = d
            hex_char = "0123456789abcdef"[best_digit]
            return hex_char + hex_char

        return "#" + closest(color[1:3]) + closest(color[3:5]) + closest(color[5:7])
