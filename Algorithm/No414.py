# run time:
# memory:
class Solution:
    def action(self, nums: [int]):
        nums = sorted(list(set(nums)))
        len_num = len(nums)
        if len_num <= 2:
            return nums[len_num-1]
        return nums[-3]

solution = Solution()
print(solution.action([2,2,3,1]))
print(solution.action([2,2,1]))
print(solution.action([1,2]))
print(solution.action([-1,2,3]))

