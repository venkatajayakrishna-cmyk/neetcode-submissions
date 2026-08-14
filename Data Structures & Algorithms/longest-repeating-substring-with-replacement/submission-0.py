class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        adj = {c:0 for c in s}
        max_len = 0
        n = len(s)
        i = 0
        j = 0
        max_frequency = 0

        while j < n:
            adj[s[j]] += 1
            max_frequency = max(max_frequency, adj[s[j]])
            operations = (j - i + 1) - max_frequency
            if operations <= k:
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                adj[s[i]] -= 1
                i += 1
                j += 1
        return max_len