list_of_numbers = [3,2,2,3]
remove_value = 3

for index1 in range(len(list_of_numbers)):
    if remove_value in list_of_numbers:
        list_of_numbers.remove(remove_value)
print(list_of_numbers)
print(len(list_of_numbers))