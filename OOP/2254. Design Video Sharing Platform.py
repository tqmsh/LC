from heapq import heappop, heappush
from collections import defaultdict
from typing import List, Dict, Optional

class VideoSharingPlatform:
    def __init__(self):
        self.cur_id = 0; self.free_id = []; self.id_to_vid: Dict[int, str] = {}; self.id_to_views = defaultdict(int); # free_id = min heap by default.
        self.id_to_likes = defaultdict(int); self.id_to_dislikes = defaultdict(int)

    def getVideoId(self) -> int:
        ans = -1
        if not self.free_id: ans = self.cur_id; self.cur_id += 1
        else: ans = heappop(self.free_id)
        return ans
    
    def upload(self, vid: str) -> int:
        id = self.getVideoId()
        self.id_to_vid[id] = vid
        return id
    
    def remove(self, id: int) -> int:
        if id in self.id_to_vid:
            heappush(self.free_id, id)
            del self.id_to_vid[id]; del self.id_to_views[id]; del self.id_to_likes[id]; del self.id_to_dislikes[id]
            return id
        return -1  # 🟥 Edge case: non-existent video
    
    def watch(self, id: int, st: int, et: int) -> str:
        if id not in self.id_to_vid: return "-1"  # 🟥 Edge case: watching non-existent video
        self.id_to_views[id] += 1
        vid = self.id_to_vid[id]
        if st >= len(vid): return ""  # 🟥 Edge case: start minute beyond video length
        return vid[st: min(len(vid), et + 1)]
    
    def like(self, id: int) -> None:
        if id in self.id_to_vid: self.id_to_likes[id] += 1
    
    def dislike(self, id: int) -> None:
        if id in self.id_to_vid: self.id_to_dislikes[id] += 1
    
    def getLikesAndDislikes(self, id: int) -> List[int]:
        if id not in self.id_to_vid: return [-1]  # 🟥 Edge case: non-existent video
        return [self.id_to_likes[id], self.id_to_dislikes[id]]
    
    def getViews(self, id: int) -> int:
        if id not in self.id_to_vid: return -1  # 🟥 Edge case: non-existent video
        return self.id_to_views[id]


# Test Cases
platform = VideoSharingPlatform()

# Initialization Test
print("Initialization Complete")

# Test #1: Upload video
id1 = platform.upload("12345")
print(f"Test #1: Uploaded video ID: {id1} -> Expected: 0")

# Test #2: Watch video within range
result = platform.watch(0, 1, 3)
print(f"Test #2: Watched content (ID 0, 1 to 3): {result} -> Expected: '234'")

# Test #3: Like video
platform.like(0)
likes_dislikes = platform.getLikesAndDislikes(0)
print(f"Test #3: Likes and Dislikes (ID 0): {likes_dislikes} -> Expected: [1, 0]")

# Test #4: Dislike video
platform.dislike(0)
likes_dislikes = platform.getLikesAndDislikes(0)
print(f"Test #4: Likes and Dislikes after dislike (ID 0): {likes_dislikes} -> Expected: [1, 1]")

# Test #5: Get views after watching
views = platform.getViews(0)
print(f"Test #5: Views (ID 0): {views} -> Expected: 1")

# Test #6: Delete video
deleted_id = platform.remove(0)
print(f"Test #6: Deleted video ID: {deleted_id} -> Expected: 0")

# Test #7: Watch deleted video
result = platform.watch(0, 1, 3)
print(f"Test #7: Watched deleted video (ID 0): {result} -> Expected: '-1'")

# Test #8: Re-upload video and check ID reuse
id2 = platform.upload("678910")
print(f"Test #8: Uploaded new video ID after deletion: {id2} -> Expected: 0")

# Test #9: Watch video out of range
result = platform.watch(0, 10, 12)
print(f"Test #9: Watched out-of-range content (ID 0, 10 to 12): '{result}' -> Expected: ''")

# Test #10: Get stats for non-existent video
views = platform.getViews(99)
print(f"Test #10: Get views for non-existent video (ID 99): {views} -> Expected: -1")
