# run time:
# memory:
class Solution:
    def action(self, nums: [], k: int):
        if len(nums) % k != 0:
            return False
        while len(nums) != 0:
            min_num = min(nums)
            nums.remove(min_num)
            for j in range(1, k):
                if (min_num + j) in nums:
                    nums.remove(min_num + j)
                else:
                    return False
        return True

solution = Solution()
print(solution.action([1,2,3,6,2,3,4,7,8], 3))
print(solution.action([1,2,3,4,5], 4))
print(solution.action([1,2,3,4,5,6], 2))
print(solution.action([2,1], 2))

