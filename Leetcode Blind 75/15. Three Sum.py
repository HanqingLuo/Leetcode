class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        nums.sort()
        print(nums)
        
        if len(nums) < 3 or nums[0] > 0: # 1st element after sorting > 0, then all elements in the list > 0
            return ans
    
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: # 去重
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -=1 
                elif sum < 0:
                    left +=1
                else: # sum == target
                    if left > i+1 and nums[left] == nums[left-1]: # check left duplication
                        left+=1
                    elif right < len(nums)-1 and nums[right] == nums[right+1]: # check right duplication
                        right -=1
                    else:
                        ans.append([nums[i], nums[left], nums[right]])
                        left+=1
                        right-=1
        return ans

            