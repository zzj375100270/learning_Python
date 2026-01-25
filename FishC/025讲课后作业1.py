#025讲课后作业1
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
nums = []
top = 0
right = len(matrix[0])-1
bottom = len(matrix)-1
left = 0
while left <= right and top <= bottom:
    for a in range(left,right+1):
        nums.append(matrix[top][a])
        a += 1
    top += 1
    for b in range(top,bottom+1):
        nums.append(matrix[b][right])
        b += 1
    right -= 1
    if top <= bottom:
        for c in range(right,left-1,-1):
            nums.append(matrix[bottom][c])
            c -= 1
        bottom -= 1
    if left <= right:
        for d in range(bottom,top-1,-1):
            nums.append(matrix[d][left])
            d -= 1
        left += 1
    print(nums)