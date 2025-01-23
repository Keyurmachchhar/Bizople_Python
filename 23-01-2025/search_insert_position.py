list_of_numbers = [1,3,5,6]
target = 2

for i in range(len(list_of_numbers)):
    # print(list_of_numbers[i])
    if list_of_numbers[i] == target:
        print(i)
        break
        
    elif target <= list_of_numbers[i]:
        print(i)
        break
    
else:
    print(len(list_of_numbers))