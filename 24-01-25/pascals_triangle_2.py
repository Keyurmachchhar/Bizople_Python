numRows = 3
ans = []
ans.append([1])
print(ans)
for index1 in range(numRows):
    numRow = [1]
    # print(numRows)
    for index2 in range(index1):
        numRow.append(ans[index1][index2] + ans[index1][index2 + 1])
        
    numRow.append(1)
    ans.append(numRow)
print(ans[numRows])