class Solution:
    def secondGreaterElement1(self,nums):
        st = []
        dic = {}
        ans = [-1] * len(nums)
        for i in range(0,len(nums)):
            while st and nums[st[-1]] < nums[i]:
                dic[st.pop()] = i
            st.append(i)
        for i in range(0,len(nums)):
            if i in dic:
                j = dic.get(i) + 1
                flag = 0
                while(j<len(nums)):
                    if nums[j] > nums[i]:
                        dic[i] = j
                        flag = 1
                        break
                    else:
                        j += 1
                if flag == 1:
                    ans[i] = nums[j]
            
        return ans
    def secondGreaterElement2(self, nums):
        ans = [-1] * len(nums)
        stack1 = []
        stack2 = []
        tmp = []
        for i in range(len(nums)):
            while stack2 and nums[i] > nums[stack2[-1]]:
                ans[stack2.pop()] = nums[i]
            while stack1 and nums[i] > nums[stack1[-1]]:
                tmp.append(stack1.pop())
            while tmp:
                stack2.append(tmp.pop())
            stack1.append(i)
        return ans
    
nums = [1,17,18,0,18,10,20,0]
ans = Solution()
print(ans.secondGreaterElement2(nums))