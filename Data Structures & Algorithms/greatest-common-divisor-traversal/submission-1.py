class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        adjList = defaultdict(set)

        if 1 in nums and nums.count(1) > 1:
            return False

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                gcd = math.gcd(nums[i], nums[j])

                if gcd > 1:
                    adjList[nums[i]].add(nums[j])
                    adjList[nums[j]].add(nums[i])
        visited = set()
        def bfs(starter):
            queue = deque([starter])
            
            while queue:
                num = queue.popleft()

                visited.add(num)

                for adj in adjList[num]:
                    if adj not in visited:
                        queue.append(adj)
            
            return 

        bfs(nums[0])

        for num in set(nums):
            if num not in visited:
                return False 
        
        return True 

        
