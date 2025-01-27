from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
ans = defaultdict(list)

for i in strs:
    key = "".join(sorted(i))
    # print(key)
    ans[key].append(i)
    # print(ans)
ans2 = list(ans.values())   
print(ans2)