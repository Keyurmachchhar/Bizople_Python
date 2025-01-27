nums = [0,0,1,1,1,1,2,3,3]
k = 2

for index in range(2,len(nums)):
    # print(nums[index])
    if nums[index] != nums[k-2]:
        nums[k] = nums[index]
        k += 1
        
print(k)