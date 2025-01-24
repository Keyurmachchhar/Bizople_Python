nums = [4,1,2,1,2]
a = set()

for i in nums:
    if i in a:
        a.remove(i)
    else:
        a.add(i)
        
print(a.pop())