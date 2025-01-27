nums = [1,2,2]
nums.sort()
ans = [[]]
new_set = set()

for index in nums:
    new_array = []
    for index2 in ans:
        sum = index2 + [index]
        if tuple(sum) not in new_set:
            new_array.append(sum)
            new_set.add(tuple(sum))
        # print(new_array)
    ans += new_array           
print(ans)