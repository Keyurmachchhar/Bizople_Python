nums = [1,2,3]
ans = [[]]

for index in nums:
    new_array = []
    for index2 in ans:
        sum = index2 + [index]
        new_array.append(sum)
        # print(new_array)
    ans += new_array           
print(ans)