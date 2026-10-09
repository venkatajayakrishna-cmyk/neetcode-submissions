class Solution:
    def LCS(self, a, b, n, m):
        if n == 0 or m == 0:
            return 0
        
        if a[n - 1] == b[m - 1]:
            return self.LCS(a, b, n - 1, m - 1) + 1
        else:
            return max(self.LCS(a, b, n - 1, m), self.LCS(a, b, n, m - 1))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    t[i][j] = 0
                else:
                    if text1[i - 1] == text2[j - 1]:
                        t[i][j] = t[i - 1][j - 1] + 1
                    else:
                        t[i][j] = max(t[i - 1][j], t[i][j - 1])
        
        return t[n][m]
    
