# https://leetcode.cn/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # contruct preProd array
        p = 1
        preProd = []
        for n in nums:
            p*=n
            preProd.append(p)
        # print(preProd)

        # contruct postProd array
        postProd = []
        p=1 
        for n in reversed(nums):
            p*=n
            postProd.append(p)
        postProd = postProd[::-1]
        # print(postProd)


        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(postProd[i+1])
            elif i == len(nums)-1:
                ans.append(preProd[i-1])
            else: 
                ans.append(preProd[i-1] * postProd[i+1])
        return ans
