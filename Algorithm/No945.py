# run time:
# memory:
class Solution:
    def action(self, nums: []):
        nums = sorted(nums)
        num_max = nums[0]
        count = 0
        for i in range(1,len(nums)):
            diff = 0
            if nums[i] <= num_max:
                diff = num_max - nums[i] +1
                count += diff
            num_max = nums[i] + diff
        return count

solution = Solution()
print(solution.action([1,2,2]))
print(solution.action([3,2,1,2,1,7]))
# print(solution.action([1]))

