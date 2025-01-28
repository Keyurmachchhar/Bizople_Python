nums = [1,2,1,3,2,5]
counts = {}
ans = []

for index in nums:
    if index in counts:
        counts[index] += 1
        print("+=1",counts)
    else:
        counts[index] = 1
        print("=1",counts)
        
# print(counts)
for key,value in counts.items():
    if value == 1:
        ans.append(key)
        
print(ans)