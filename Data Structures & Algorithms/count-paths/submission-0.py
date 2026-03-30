class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rights = n - 1
        down = m - 1

        return math.comb(rights+down, rights)