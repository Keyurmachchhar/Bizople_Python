nums = [-2,1,-3,4,-1,2,1,-5,4]
res = nums[0]
ans = 0

for i in nums:
    # print(i)
    if 0 > ans:
        ans = 0
    ans += i
    # print("ans:",ans)
    res = max(res,ans)
    # print(res,ans)
    # print("res:",res)
print(res)
