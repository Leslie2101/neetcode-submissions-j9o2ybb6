class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable = deque([(0, 0)])
        while reachable:
            node, t = reachable.popleft()
            val = nums[node]
            nums[node] = -1

            if node == len(nums) -1:
                return t

            for i in range(1, val+1):
                if node + i < len(nums) and nums[node+i] != -1:
                    reachable.append((node + i, t+1))

        return -1



        
        