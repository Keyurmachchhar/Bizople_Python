nums = [-2]
ans = []

if len(nums) == 1:
    ans = nums

for i in range(len(nums)-1):
    # print(f"{nums[i]},{nums[i+1]}")
    a = nums[i] * nums[i+1]
    ans.append(a)
    
# ans.sort()
# print(ans[-1])
print(max(ans))