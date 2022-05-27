# https://leetcode.cn/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in nums, if target - nums[i] in hashtable, return [i, hashtable[target-nums[i]]]
        hashtable = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hashtable:
                hashtable[nums[i]] = i
            else: 
                return [i, hashtable[diff]]