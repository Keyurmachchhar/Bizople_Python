nums = [1,2,0]

num = [x for x in nums if x >= 0]
num.sort()
print(num)

target = 1
for index in num:
    # print(index)
    if index == target:
        target += 1
    elif index > target:
        break
        
print(target)