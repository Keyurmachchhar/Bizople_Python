list_of_numbers = [1, 3, 5, 4, 2]
pivot = -1
for index1 in range(len(list_of_numbers) - 2,-1,-1):
    # print(list_of_numbers[index1])
    if list_of_numbers[index1] < list_of_numbers[index1 + 1]:
        pivot = index1
        break
if pivot != -1:
    for index2 in range(len(list_of_numbers) - 1,pivot,-1):
        if list_of_numbers[index2] > list_of_numbers[pivot]:
            list_of_numbers[pivot],list_of_numbers[index2] = list_of_numbers[index2],list_of_numbers[pivot]
            break
        
list_of_numbers[pivot + 1:] = reversed(list_of_numbers[pivot + 1:])

print(list_of_numbers)