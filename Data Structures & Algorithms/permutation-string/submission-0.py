class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        countOfChar = defaultdict(int)
        for char in s1:
            countOfChar[char] += 1
        k = len(s1)
        n = len(s2)
        count = len(countOfChar)

        while j < n:
            if s2[j] in countOfChar:
                    countOfChar[s2[j]] -= 1
                    if countOfChar[s2[j]] == 0:
                        count -= 1
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if count == 0:
                    return True
                if s2[i] in countOfChar:
                    if countOfChar[s2[i]] == 0:
                        count += 1
                    countOfChar[s2[i]] += 1                 
                i += 1
                j += 1

        return False