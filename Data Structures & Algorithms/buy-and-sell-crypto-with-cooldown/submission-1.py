class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold2 = nohold2 = 0 # cost 2 days from now 
        hold1 = nohold1 = 0 # benefit 1 day from onw 


        if len(prices) < 2:
            return 0

        res = 0
        hold2 = -prices[0]
        hold1 = max(-prices[1], hold2)
        nohold1=max(0, hold2+prices[1])
        print(hold1, nohold1)
        print(hold2, nohold2)

        res = max(hold1, nohold1)
        for i in range(2, len(prices)):
            print(f"{hold2=}, {nohold2=}")
            print(f"{hold1=}, {nohold1=}")
            # update current keep, current not 
            curhold = max(nohold2 - prices[i], hold1)
            curnohold = max(hold1 + prices[i], nohold1)

            res = max(curhold, curnohold)
            # move up 
            hold2, nohold2 = hold1, nohold1
            hold1, nohold1 = curhold, curnohold 

            print(f"{i=},{curhold=},{curnohold=}")

        return res


