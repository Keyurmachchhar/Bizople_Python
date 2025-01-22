list_of_numbers = [-1, 2, 1, -4]
target = 1
list_of_numbers.sort()
print(list_of_numbers)

nearest_sum = float('inf')  

for index1 in range(len(list_of_numbers) - 2):
    left = index1 + 1  
    right = len(list_of_numbers) - 1
    
    while left < right:
        sum = list_of_numbers[index1] + list_of_numbers[left] + list_of_numbers[right]
        print(f"({list_of_numbers[index1]}) + ({list_of_numbers[left]}) + ({list_of_numbers[right]}) is:{sum}")
        
        if abs(sum - target) < abs(nearest_sum - target):
            nearest_sum = sum
            # print(nearest_sum)
        
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            print(sum)
            nearest_sum = sum
            break

print(f"Your target is:{target}\nYour nearest value of target is:{nearest_sum}")
