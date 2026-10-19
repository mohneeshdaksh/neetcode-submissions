class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.follow_map[userId].add(userId)
        for followee in self.follow_map[userId]:
            if followee in self.tweet_map:
                index = len(self.tweet_map[followee]) - 1
                count, tweetId = self.tweet_map[followee][index]
                minHeap.append([count, tweetId, followee, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)