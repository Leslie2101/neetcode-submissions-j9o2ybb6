class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)

        l = 0
        r = 0
        resLeft, resRight = None, None

        freq = defaultdict(int)

        def check():
            # max 52 iteration -> O(1)
            for key, val in counter.items():
                if key not in freq or freq[key] < val:
                    return False 
            
            return True

        while r < len(s):

            # increase by right pointer 
            freq[s[r]] += 1

            # shrink left to find smallest satisfying subarray
            found = False
            while l <= r and check():
                found = True
                freq[s[l]] -= 1
                l += 1

            # update smallest length 
            if found:
                curLen = r - l + 2

                if resLeft == None or resRight - resLeft + 1 > curLen:
                    resLeft = l - 1
                    resRight = r 
            
            r += 1
                
        return s[resLeft:resRight+1] if resLeft != None else ""