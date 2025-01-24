nums = [2,0,2,1,1,0]

for index1 in range(len(nums)):
    for index2 in range(index1+1,len(nums)):
        # print(f"{nums[index1]},{nums[index2]}")
        if nums[index1] >= nums[index2]:
            nums[index1],nums[index2] = nums[index2],nums[index1]
            
print(nums)