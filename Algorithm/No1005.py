# run time:
# memory:
class Solution:
    def action(self, nums: [], k: int):
        while k > 0:
            min_nums = min(nums)
            min_index = nums.index(min_nums)
            nums[min_index] = -min_nums
            k-=1
        return sum(nums)

solution = Solution()
print(solution.action([4,2,3], 1))
print(solution.action([3,-1,0,2], 3))
print(solution.action([2,-3,-1,5,-4], 2))

