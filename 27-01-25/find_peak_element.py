nums = [1,2,1,3,5,6,4]
max_val = max(nums)
ans = 0
for i in range(len(nums)):
    # print(i)
    if nums[i] == max_val:
        ans = i
print(ans)