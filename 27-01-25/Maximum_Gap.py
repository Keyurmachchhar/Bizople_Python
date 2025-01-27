nums = [3,6,9,1]
nums.sort()
# print(nums)
ans = 0

for index in range(len(nums)-1):
    val = nums[index+1] - nums[index]
    ans = max(ans,val)

print(ans)
    