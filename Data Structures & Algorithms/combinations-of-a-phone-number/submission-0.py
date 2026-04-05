from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        prods = product(*(maps[ch] for ch in digits))
        res = []

        print(prods)

        for prod in prods:
            cur = ''.join(prod)

            if cur:
                res.append(cur)
        


        return res





