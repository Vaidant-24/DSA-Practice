def nextGreaterElement(nums1,nums2):
        ans = []
        for i in nums1:
            if i == nums2[-1]:
                ans.append(-1)
            else:
                j = -1
                while(nums2[j] != i):
                    x = nums2[j]
                    j -= 1
                j += 1
                while x <= i and j <= -1:
                    x = nums2[j]
                    j += 1
                if x > i:
                    ans.append(x)
                else:
                    ans.append(-1)
        return ans

def nextGreaterOp(num1, num2):
    st = []
    dic = {}
    ans = []
    for i in nums2:
        while st and st[-1] < i:
            dic[st.pop()] = i
        st.append(i)
    
    for j in nums1:
        ans.append(dic.get(j,-1))
        
    return ans
    
nums1 = [1,3,2,5,4]
nums2 = [3,2,5,4,1,7]

print(nextGreaterElement(nums1, nums2))
print(nextGreaterOp(nums1, nums2))