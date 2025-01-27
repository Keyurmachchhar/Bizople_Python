class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        new_array1 = []

        for index1 in range(len(nums)):
            val = nums[index1]
            new_array2 = nums[:index1] + nums[index1+1:]

            for index2 in self.permute(new_array2):
                new_array1.append([val] + index2)
        return new_array1
    
s = Solution()
nums = [1,2,3]

print(s.permute(nums))