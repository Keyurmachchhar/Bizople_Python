nums = [3,2,1,0,4]
fp = len(nums) - 1

for i in range(len(nums) - 2,-1,-1):
    if i + nums[i] >= fp:
        fp = i
        
if fp == 0:
    print("true")
else:
    print("false")