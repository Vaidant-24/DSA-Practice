class Solution:
    def nextGreaterElements(self,nums):
        st = []
        ans = [-1] * len(nums)
        for loop in range(2):
            for i in range(0,len(nums)):
                while st and nums[st[-1]] < nums[i]:
                    ans[st.pop()] = nums[i]
                st.append(i)
        return ans
nums = [5,2,1,3]
sol = Solution()

print(sol.nextGreaterElements(nums))