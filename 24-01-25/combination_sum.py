candidates = [2,3,6,7]
target = 7
candidates.sort()
ans = []

tmp = [[x] for x in candidates if x <= target]
print(tmp)

for index1 in tmp:
    # print("index1",index1)
    tmp_sum = sum(index1)
    
    if tmp_sum == target:
        ans.append(index1)
        continue
        
    for index2 in candidates:
        # print("index2",index2)
        if index2 >= index1[-1] and tmp_sum + index2 <= target:
            tmp.append(index1 + [index2])
ans.sort()           
print(ans)