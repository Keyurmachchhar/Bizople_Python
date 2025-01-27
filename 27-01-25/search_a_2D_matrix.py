matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
ans = False

for i in matrix:
    if target in i:
        ans = True

print(ans)