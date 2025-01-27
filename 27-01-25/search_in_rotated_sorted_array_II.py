nums = [2,5,6,0,0,1,2]
target = 3
ans = False

nums.sort()
print(nums)

for index in nums:
    if index == target:
        ans = True
print(ans)