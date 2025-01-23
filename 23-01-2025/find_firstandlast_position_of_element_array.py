list_of_numbers = [2,3,1,1,1,3]
target = 1
ans = []

if len(list_of_numbers) == 1 and target in list_of_numbers:
    ans.append(0)
    ans.append(0)

for i in range(len(list_of_numbers)):
    # print(list_of_numbers[i])
    if list_of_numbers[i] == target:
        ans.append(i)

if target not in list_of_numbers:
    value = -1
    ans.append(value)
    ans.append(value)
        
print()