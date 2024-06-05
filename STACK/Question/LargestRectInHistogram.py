def largestRectangleArea(arr):
    n = len(arr)
    st = []
    leftsmall = [0] * n
    rightsmall = [0] * n
    
    for i in range(n):
        while st and arr[i] <= arr[st[-1]]:
            st.pop()
        
        leftsmall[i] = st[-1] + 1 if st else 0
        st.append(i)
    
    st.clear()
    
    for i in range(n-1, -1, -1):
        while st and arr[i] <= arr[st[-1]]:
            st.pop()
            
        rightsmall[i] = st[-1] - 1 if st else n-1
        st.append(i)
        

    maxArea = 0
    for i in range(n):
        Area = (rightsmall[i] - leftsmall[i] + 1) * arr[i]
        maxArea = max(maxArea, Area)
        
    return maxArea

arr = [2,5,6,2,5,1,3]
print(largestRectangleArea(arr))