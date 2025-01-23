list1 = [1,2,3,0,0,0]
list2 = [2,5,6]
m=3
n=3

p1 = m - 1
p2 = n - 1
p = m + n - 1

while p2 >= 0:
    if p1 >= 0 and list1[p1] > list2[p2]:
        list1[p] = list1[p1]
        p1 -= 1
    else:
        list1[p] = list2[p2]
        p2 -= 1
    p -= 1
    
print(list1)