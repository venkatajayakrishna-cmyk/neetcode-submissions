class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        visited = set()
        max_length = 0

        while j < n:
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                max_length = max(j - i, max_length)
            else:
                while s[j] in visited:
                    visited.discard(s[i])
                    i += 1
        return max_length