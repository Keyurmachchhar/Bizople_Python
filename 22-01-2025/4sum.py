list_of_numbers = [1,0,-1,0,-2,2]
list_of_numbers.sort()
print(list_of_numbers)
result = []
for index1 in range(len(list_of_numbers)):
    # print(list_of_numbers[index1])
    for index2 in range(index1+1,len(list_of_numbers)):
        # print(f"{list_of_numbers[index1]},{list_of_numbers[index2]}")
        for index3 in range(index2+1,len(list_of_numbers)):
            # print(f"{list_of_numbers[index1]},{list_of_numbers[index2]},{list_of_numbers[index3]}")
            for index4 in range(index3+1,len(list_of_numbers)):
                # print(f"{list_of_numbers[index1]},{list_of_numbers[index2]},{list_of_numbers[index3]},{list_of_numbers[index4]}")
                if list_of_numbers[index1] + list_of_numbers[index2] + list_of_numbers[index3] + list_of_numbers[index4] == 0:
                    list1 = [list_of_numbers[index1],list_of_numbers[index2],list_of_numbers[index3],list_of_numbers[index4]]
                    print(list1)
                    if list1 not in result:
                        result.append(list1)
                    
print("Sum of each element is zero.")         
print(f"Your ans:{result}")
