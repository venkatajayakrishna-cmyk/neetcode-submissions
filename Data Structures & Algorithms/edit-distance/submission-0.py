class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    t[0][j] = j
                elif j == 0:
                    t[i][0] = i
                
                else:
                    if word1[i - 1] == word2[j - 1]:
                        t[i][j] = t[i - 1][j - 1]
                    else:
                        t[i][j] = 1 + min(t[i - 1][j], t[i][j - 1], t[i - 1][j - 1])

        return t[n][m]