class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1, 2, 3, 4]
        # cost= [2, 2, 4, 1]

        # diff= [-1, 0, -1, 3]
        # must start at >0 diff 

        diffs = [gas[i]-cost[i] for i in range(len(gas))]
        

        # find candidate starting point 
        start = 0
        while start < len(gas):
            if diffs[start] >= 0:
                break 
            
            start += 1

        if start == len(gas):
            return -1
        
        # start explore: 
        # if at some point we lack gas: move start to the left
        idx = (start + 1)%len(gas)
        curGas = diffs[start]
        revisited = False

        print(f"{start=}")
        
        while idx != start:
            
            curGas += gas[idx]


            # not enough gas to move to next station -> move start to the left side  
            while ((curGas < cost[idx]) or (cost[start] > gas[start])):

                # go through the cycle but gas still < 0 
                if start == idx:
                    return -1

                start = (start - 1)%len(gas)
                curGas += diffs[start]
            
            print(f"{start=}, {idx=}, {curGas=}")

            # move to next station
            curGas -= cost[idx]
            idx = (idx + 1)%len(gas)
        
        return start


            

