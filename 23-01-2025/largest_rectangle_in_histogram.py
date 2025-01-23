list_of_numbers = [2,4]
area = 0

for index1 in range(len(list_of_numbers)):
    min_height = list_of_numbers[index1]
    for index2 in range(index1,len(list_of_numbers)):
        min_height = min(min_height,list_of_numbers[index2])
        a = min_height * (index2 - index1 + 1)
        area = max(area,a)
        
print(area)