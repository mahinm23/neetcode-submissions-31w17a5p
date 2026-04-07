class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0]*26
        max_freq = 0
        l = 0
        r = 0
        max_len = 0

        for r in range(0, len(s)):
            char_index = ord(s[r]) - ord('A')
            chars[char_index] += 1

            max_freq = max(max_freq, chars[char_index])

            # Check if window invalid
            # So remove the left elements
            while (r-l+1) - max_freq > k:
                left_char = ord(s[l]) - ord('A')
                chars[left_char] -= 1
                l += 1

            # Window is valid
            max_len = max(max_len, r - l + 1)

        return max_len