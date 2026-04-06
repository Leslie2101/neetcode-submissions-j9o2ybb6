class Twitter:

    def __init__(self):
        self.user2tweets = defaultdict(list) # user id -> tweets 
        self.user2followees = defaultdict(set) # user id -> followee 
        self.time = 0 


    def postTweet(self, userId: int, tweetId: int) -> None:
        # update user2tweets
        self.user2tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(f"{self.user2followees}")
        # print(f"{self.user2tweets}")

        res = []

        heap = []
        for followeeId in self.user2followees[userId] | {userId}:
            if self.user2tweets[followeeId]:
                t, tweetId = self.user2tweets[followeeId][-1]
                heapq.heappush(heap, (-t, tweetId, followeeId, 1))
        
        n = 0
        while n < 10 and heap:
            t, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            n += 1

            # push next most recent tweet of this followeeId to the heap 
            idx += 1
            if abs(idx) <= len(self.user2tweets[followeeId]):
                newT, newTweetId = self.user2tweets[followeeId][-idx]
                heapq.heappush(heap, (-newT, newTweetId, followeeId, idx))

        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user2followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user2followees[followerId].discard(followeeId)
