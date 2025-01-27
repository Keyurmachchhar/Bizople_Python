nums = [100,4,200,1,3,2]
nums.sort()
new_set = set(nums)
ans,length = 0,0

for index1 in nums:
    if index1 - 1 not in new_set:
        length = 1
        
        while index1 + length in new_set:
            length += 1
        
        ans = max(ans,length)

print(ans)