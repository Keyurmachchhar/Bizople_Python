nums = [1,2,3,1]
a = set(nums)

# ans = False

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             ans = True
            
# print(ans)

if len(nums) != len(a):
    print(True)
else:
    print(False)