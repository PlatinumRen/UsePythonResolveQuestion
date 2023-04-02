from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        total = 0
        satisfaction.sort()
        for i in range(n):
            temp = 0
            for j in range(i, n):
                temp += satisfaction[j] * (j - i + 1)
            if temp > total:
                total = temp
        return total if total > 0 else 0