class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1: O(n)
        ans = 0
        while n:
            ans += (n % 2)
            n = n >> 1 # right shift 1 bit
        return ans
        
        # Solution 2: O(log(n))
        # ans = 0
        # while n:
        #     n &= (n-1)
        #     ans += 1
        # return ans 