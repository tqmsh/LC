from typing import List
from collections import Counter, defaultdict

def _isok(nums: List[int]) -> bool: 
    if len(nums) % 3 != 0: return 0
    nums = sorted(nums) 
    cnt = Counter(nums) # num -> cnt
    for num in nums: 
        cnt[num] %= 3 # 拼三个
        amt = min(cnt[num], cnt[num + 1], cnt[num + 2])
        cnt[num] -= amt
        cnt[num + 1] -= amt
        cnt[num + 2] -= amt
        if cnt[num]: return 0
    return 1

def valid(arr: List[str]) -> bool:
    col_to_nums = defaultdict(list) # col -> nums
    for card in arr:
        col = card[0]
        nums = int(card[1:])
        col_to_nums[col].append(nums) 
    for _, nums in col_to_nums.items():  
        if not _isok(nums): return 0 
    return 1


def main():
    tiles = ["R2", "R2", "R2", "R3", "R4", "R4", "B1", "B1", "B1", "G6", "G7", "G8"]
    print(valid(tiles))

if __name__ == "__main__":
    main()