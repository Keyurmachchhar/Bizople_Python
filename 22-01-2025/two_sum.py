length_of_list = int(input("Enter the length of list:"))
target_sum = int(input("Enter the target sum:"))
num = 0
list1 = []
list2 = []
for index in range(length_of_list):
    num += 1
    list_value = int(input(f"Enter {num} value of list:"))
    list1.append(list_value)

print(list1)
print(f"Your target sum is:{target_sum}")
for index1 in range(len(list1)):
    for index2 in range(index1 + 1,len(list1)):
        # print(f"{list1[index1]} and {list1[index2]}")
       if list1[index1] + list1[index2] == target_sum:
           value_of_index1andindex2 = index1,index2
           list2.append(value_of_index1andindex2)
        #    print(f"[{index1},{index2}]")
           
print(list2)