from typing import List
from itertools import count
from collections import defaultdict, deque
from heapq import heappush, heapreplace, merge  

class Twitter:
    def __init__(self):
        self.timer = count(step = -1)
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)
    def postTweet(self, user_ID: int, tweet_ID: int) -> None:
        self.tweets[user_ID].appendleft(next(self.timer), tweet_ID)
        if len(self.tweets[user_ID]) > 10: self.tweets[user_ID].pop()
    def getNewsFeed(self, user_ID: int) -> List[int]:
        tweets = list( merge( *( self.tweets[followee] for followee in self.followees[user_ID] | {user_ID} ) ) )   
                                                        # 博主 + 自己的信息, 按照时间从小到大排序 
        return [tweet_id for _, tweet_id in tweets[: 10]]
    def follow(self, follower_ID: int, followee_ID: int) -> None:
        self.followees[follower_ID].add(followee_ID)
    def unfollow(self, follower_ID: int, followee_ID: int) -> None:
        self.followees[follower_ID].discard(followee_ID)
    from typing import List
from itertools import count
from collections import defaultdict, deque
from heapq import merge

class Twitter:
    def __init__(self):
        self.timer = count(step=-1)
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, user_ID: int, tweet_ID: int) -> None:
        self.tweets[user_ID].appendleft((next(self.timer), tweet_ID))
        if len(self.tweets[user_ID]) > 10:
            self.tweets[user_ID].pop()

    def getNewsFeed(self, user_ID: int) -> List[int]:
        tweets = list(merge(*(self.tweets[followee] for followee in self.followees[user_ID] | {user_ID}))) # 博主 + 自己的信息, 按照时间从小到大排序 
        
        return [tweet_id for _, tweet_id in tweets[:10]]

    def follow(self, follower_ID: int, followee_ID: int) -> None:
        self.followees[follower_ID].add(followee_ID)

    def unfollow(self, follower_ID: int, followee_ID: int) -> None:
        self.followees[follower_ID].discard(followee_ID)

# Test case
twitter = Twitter()

# User 1 posts a tweet
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))  # Should print [5]

# User 1 posts another tweet
twitter.postTweet(1, 3)
print(twitter.getNewsFeed(1))  # Should print [3, 5]

# User 2 posts a tweet
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(2))  # Should print [6]

# User 1 follows User 2
twitter.follow(1, 2)
print(twitter.getNewsFeed(1))  # Should print [6, 3, 5]

# User 1 unfollows User 2
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # Should print [3, 5]
