class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window 
        ans = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0: 
                currSum = 0 # reset currSum
            currSum+=n # CurrSum 窗口一直向后加，直到出现负数，然后重置
            ans = max(currSum, ans)
        return ans