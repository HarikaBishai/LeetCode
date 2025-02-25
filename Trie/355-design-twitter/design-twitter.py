class Twitter:

    def __init__(self):
        self.followHash = defaultdict(set)
        self.tweetsHash = defaultdict(list)
        self.count = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count-=1
        self.tweetsHash[userId].append((tweetId,  self.count))

    def getNewsFeed(self, userId: int) -> List[int]:
        friends_list = list(self.followHash[userId])
        friends_list.append(userId)
        maxHeap = []
        for user in friends_list:
            if user in self.tweetsHash:
                
                index = len(self.tweetsHash[user])-1
                tweet = self.tweetsHash[user][index]
                heapq.heappush(maxHeap, (tweet[1], tweet[0],user,  index-1))
        
        result = []
        while maxHeap and len(result)< 10:
            count, tweet_id , user, index = heapq.heappop(maxHeap)
            result.append(tweet_id)
            if index >= 0:
                tweet = self.tweetsHash[user][index]
                heapq.heappush(maxHeap, (tweet[1], tweet[0], user, index-1))

        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followHash[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followHash[followerId]:
            self.followHash[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)