from collections import deque

class Solution:
    def differ_by_one(self, word1, word2):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1
    
    def bfs(self, adj, start, end):
        queue = deque()
        queue.append((start, 1))
        visited =set()
        visited.add(start)

        while queue:
            node, level = queue.popleft()

            if node == end:
                    return level

            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
                
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        patterns = {}
        words = wordList + [beginWord]

        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[(i + 1):]
                patterns.setdefault(pattern, []).append(word)
            
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[(i + 1):]
                for neighbor in patterns[pattern]:
                    if neighbor != word:
                        adj.setdefault(word, []).append(neighbor)

        return self.bfs(adj, beginWord, endWord)