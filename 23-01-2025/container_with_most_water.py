list_of_numbers = [2,4]

left = 0
right = len(list_of_numbers) - 1#8
ans = 0

while left < right:
    ans = max(ans,(right - left) * min(list_of_numbers[left],list_of_numbers[right]))
    
    if list_of_numbers[left] <= list_of_numbers[right]:
        left += 1
    else:
        right -= 1

print(ans)