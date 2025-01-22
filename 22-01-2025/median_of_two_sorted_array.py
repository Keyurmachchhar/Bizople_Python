array1 = [1,2,3]
array2 = [7,5,6]

merged_array = array1 + array2
merged_array.sort()
print(merged_array)

if len(merged_array) % 2 == 0:
    n = len(merged_array) // 2
    ans = (merged_array[n-1] + merged_array[n]) // 2
    print(ans)
else:
    n = len(merged_array) // 2
    print(merged_array[n])