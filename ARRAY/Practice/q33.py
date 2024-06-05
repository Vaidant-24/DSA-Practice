nums = [[1,1,1],[1,0,1],[1,1,1]]
# Using Brute Force:-
def markRow(i,col):
    for j in range(col):
        if nums[i][j] != 0:
            nums[i][j] = -1

def markCol(j,row):
    for i in range(row):
        if nums[i][j] != 0:
            nums[i][j] = -1

def SetMatrixZero(nums):
    row = len(nums)
    col = len(nums[0])

    for i in range(row):
        for j in range(col):
            if nums[i][j] == 0:
                markRow(i,col)
                markCol(j,row)
    
    for i in range(row):
        for j in range(col):
            if nums[i][j] == -1:
                nums[i][j] = 0

    return nums

# print(SetMatrixZero(nums))

# Using Better:-
nums = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
def SetMatrixZeroBetter(nums):
    row = len(nums)
    col = len(nums[0])

    ROW = [0] * row
    COL = [0] * col

    for i in range(row):
        for j in range(col):
            if nums[i][j] == 0:
                ROW[i] = 1
                COL[j] = 1
    
    for i in range(row):
        for j in range(col):
            if ROW[i] == 1 or COL[j] == 1:
                nums[i][j] = 0
    return nums

print(SetMatrixZeroBetter(nums))

nums = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
def setMatrixZeroOptimal(nums):
    col0 = 1
    row = len(nums)
    col = len(nums[0])

    for i in range(row):
        for j in range(col):
            if nums[i][j] == 0:
                nums[i][0] = 0

                if j != 0:
                    nums[0][j] = 0
                else:
                    col0 = 0
    
    for i in range(1,row):
        for j in range(1,col):
            if nums[i][0] == 0 or nums[0][j] == 0:
                nums[i][j] = 0

    if nums[0][0] == 0:
        for j in range(col):
            nums[0][j] = 0
    if col0 == 0:
        for i in range(row):
            nums[i][0] = 0

    return nums

print(setMatrixZeroOptimal(nums))