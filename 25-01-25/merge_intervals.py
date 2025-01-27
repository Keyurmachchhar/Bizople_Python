intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = []

sum = intervals[0] + intervals[1]
sum.sort()
val = sum[0],sum[-1]
ans.append(list(val))

if len(intervals) > 2:
    ans += intervals[2:]

print(ans)