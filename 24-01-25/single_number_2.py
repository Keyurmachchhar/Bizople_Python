nums = [0,1,0,1,0,1,99]
a = {}

for index in nums:
    # print(index)
    if index in a:
        a[index] += 1
    else:
        a[index] = 1

for key,value in a.items():
    # print(key,value)
    if value == 1:
        print(key)