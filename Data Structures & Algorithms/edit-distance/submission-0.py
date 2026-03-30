class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[math.inf] * (len(word2)+1) for _ in range(len(word1)+1)]
        dp[0][0] = 0



        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i==0 or j == 0:
                    dp[i][j] = max(i, j)
                    continue 
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j])
                
                dp[i][j] = min(
                    dp[i][j],
                    dp[i-1][j-1] + 1,
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1
                )
        
        return dp[len(word1)][len(word2)]