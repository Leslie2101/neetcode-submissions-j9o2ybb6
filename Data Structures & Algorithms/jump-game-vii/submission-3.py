class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        furthestIndex = 0
        while queue:
            start = queue.popleft()

            for j in range(max(start+minJump, furthestIndex+1), min(start+maxJump+1, len(s))):
                if s[j] == '0':
                    queue.append(j)

                    if j == len(s) - 1:
                        return True 

            furthestIndex = max(furthestIndex, start+maxJump)
        return False




            
