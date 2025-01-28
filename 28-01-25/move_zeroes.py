nums = [0,0,1]
zeroes = []
for index in nums:
    # print(index)
    if index == 0:
        nums.remove(index)
        nums.append(index)
    
# nums += zeroes
print(nums)