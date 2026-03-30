from functools import cache
import sys

sys.setrecursionlimit(1000000)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @cache
        def dfs(isAlice, idx):
            if idx >= len(stoneValue):
                return 0, 0

            # maximum score for player when start playing at idx 
            myMaxScore = None
            otherScore = None 
            curPlayer = 0

            for i in range(min(3, len(stoneValue)-idx)):
                curPlayer += stoneValue[idx+i]
                
                opScore, myScore = dfs(not isAlice, idx+i+1) # score gained by Bob 
                # play optimally
                if myMaxScore == None or curPlayer + myScore > myMaxScore:
                    myMaxScore = curPlayer + myScore
                    otherScore = opScore

            # print(f"{idx=}, {isAlice=}, {myMaxScore=}, {otherScore=}")
            return myMaxScore, otherScore 
        
        alice, bob = dfs(True, 0)
        print(alice, bob)

        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"
        else:
            return "Tie"