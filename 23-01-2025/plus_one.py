digits = [1,2,3]
ans = []

value_of_int = int("".join(map(str,digits)))
value_of_int += 1
# print(value_of_int)

value_of_str = str(value_of_int)
# print(value_of_str)
for index in value_of_str:
    ans.append(int(index))
print(digits)   
print(ans)