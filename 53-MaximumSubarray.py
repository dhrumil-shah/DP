"""
53 - Maximum Subarray
"""

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.DPSolution(nums)
    
    def loopSolution(self, nums: List[int]) -> int:
        currentMax = 0
        globalMax = -sys.maxsize-1
        for i in range(len(nums)):
            currentMax += nums[i]
            
            if (currentMax > globalMax):
                globalMax = currentMax            
            
            if (currentMax < 0):
                currentMax = 0 
            
        return globalMax
    
    def DPSolution(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0]*length
        
        dp[0] = nums[0]
        total = dp[0]
        
        for i in range(1, length):
            dp[i] = nums[i] + max(dp[i-1], 0)
            total = max(dp[i], total)
        
        return total