candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
candidates.sort()

ans = []
tmp = [[[], 0, 0]]

for index1, index2, index3 in tmp:
    if index2 == target:
        ans.append(index1)
        continue
    
    for index4 in range(index3, len(candidates)):
        if index4 > index3 and candidates[index4] == candidates[index4 - 1]:
            continue
        
        if index2 + candidates[index4] > target:
            break
        
        tmp.append([index1 + [candidates[index4]], index2 + candidates[index4], index4 + 1])
        
ans.sort()
print(ans)