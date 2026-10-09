class Solution:
    def CoinChange(self, coins, amount, n):
        if n == 0:
            return 1 if amount == 0 else 0
        

        if amount >= coins[n - 1]:
            return self.CoinChange(coins, amount - coins[n - 1], n) + self.CoinChange(coins, amount, n - 1)
        else:
            return self.CoinChange(coins, amount, n - 1)

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        t = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(amount + 1):
                if i == 0:
                    t[i][j] = 1 if j == 0 else 0
                else:
                    if j >= coins[i - 1]:
                        t[i][j] = t[i][j - coins[i - 1]] + t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]
        
        return t[n][amount]