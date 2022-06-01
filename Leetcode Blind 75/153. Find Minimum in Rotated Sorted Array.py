class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search 
        # Sorted Array -> nums[left] <= nums[right]
        # if nums[mid] > nums[right]: minimum on the right

        left, right = 0, len(nums)-1
        while left < right: 
            mid = left + (right - left) // 2 
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid
        return nums[left]