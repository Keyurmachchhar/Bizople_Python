list_of_numbers = [0,0,1,1,1,2,2,3,3,4]
list_of_numbers.sort()
write_index = 1
for index in range(1,len(list_of_numbers)):
    if list_of_numbers[index] != list_of_numbers[index - 1]:
        list_of_numbers[write_index] = list_of_numbers[index]
        write_index += 1
        
print(write_index)