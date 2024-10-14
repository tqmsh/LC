from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        prev_gas = 0
        ans = 0
        for i in range(len(gas)):
            prev_gas += gas[i] - cost[i]
            if prev_gas < 0:
                prev_gas = 0
                ans = i + 1
        return ans

