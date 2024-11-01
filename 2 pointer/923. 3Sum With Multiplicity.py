from math import comb
from collections import Counter
class Solution: 
    def threeSumMulti(self, arr, target):
        M = 10 ** 9 + 7; ans = 0; f = Counter(arr); arr = sorted(list(set(arr)))  
        i = 0
        while i < len(arr): 
            if arr[i] > target: break 
            l = i; r = len(arr) - 1 
            while l <= r:
                sum = arr[i] + arr[l] + arr[r] 
                if sum == target: 
                    # 枚举可能情况
                    if arr[i] == arr[l] == arr[r]: ans += comb(f[arr[i]], 3) 
                    elif arr[i] == arr[l] != arr[r]: ans += comb(f[arr[i]], 2) * f[arr[r]]
                    elif arr[i] != arr[l] == arr[r]: ans += comb(f[arr[r]], 2) * f[arr[i]]
                    else: ans += f[arr[i]] * f[arr[l]] * f[arr[r]]   
                    l += 1
                    r -= 1
                elif sum < target: l += 1
                else: r -= 1  
            i += 1
        return ans % M
    
print(Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))