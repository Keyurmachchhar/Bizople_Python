list_of_numbers = [4,5,6,7,0,1,2]
target = 10

for index in range(len(list_of_numbers)):
    if list_of_numbers[index] == target:
        print (index)
        break
    else:
        print("-1")
    