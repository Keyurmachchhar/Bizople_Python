nums = [1,0,1,1]
k = 1
ans = False

for index1 in range(len(nums)):
    for index2 in range(index1+1,len(nums)):
        # print(f"{nums[index1]},{nums[index2]}")
        if nums[index1] == nums[index2] and abs(index1 - index2) <= k:
            ans = True

print(ans)