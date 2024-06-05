def prevSmaller(A):
        st = []
        ans = [-1]*len(A)
        for i in range(len(A)-1,-1,-1):
            while st and A[i] < A[st[-1]]:
                ans[st.pop()] = A[i]
            st.append(i)
        return ans
    
nums = [4,5,2,10,8]
print(prevSmaller(nums))