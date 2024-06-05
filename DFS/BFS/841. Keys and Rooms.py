# Question:
# Given an array rooms where each index contains a list of keys available in that room, determine if all rooms can be visited starting from room 0.

# Input:
# The input is a list of lists of integers, where each sublist represents the keys found in a
# particular room. This defines the connectivity between the rooms and available keys.

# Output:
# The output is a boolean value indicating whether it is possible to visit all rooms starting from
# room 0, based on the keys found in each room.
from collections import deque
from typing import List
class Solution:   
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:  
        q = deque(); vis = set()

        def check(x):
            global q, vis
            # 没有越界，没有走过，不是障碍 
            if x in vis: return 0 
            return 1
        
        def bfs():
            global q, vis
            while q:
                u = q.popleft()
                # 进队出有很多种情况 - 出队只有一种
                vis.add(u)
                for v in rooms[u]: 
                    if check(v): 
                        q.append(v)
                        vis.add(v) 
        
        # 把所有的出发点都放到 q 里面 
        q.append(0)
        bfs() 
        return len(rooms) == len(vis) 
    
def display_grid(array):
    for row in array:
        for element in row:
            print(f"{element}\t", end="")
        print()  # Newline after each row

def main(): 
    solution = Solution() 
    rooms = [[1,3],[3,0,1],[2],[0]]
    out = solution.canVisitAllRooms(rooms)
    print(out) 

if __name__ == "__main__":
    main()