class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # [(4, 2), (1, 3)]
        # [(7,1), (4,2), (1,2), (0,1)]
        #    3   ,   3 ,   4.5, 10

        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]

        cars.sort(reverse=True)

        stack = deque()

        print(cars)

        for pos, spd in cars:
            print(stack)
            t = (target - pos)/spd

            # a car in front of it
            if stack and (target - stack[-1][0])/stack[-1][1] >= t:
                continue
            else:
                stack.append((pos, spd))
        
        return len(stack)

