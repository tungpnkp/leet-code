class Solution:
    def convertToTitle(self, nums:[]):
        num_sort = sorted(nums)
        return num_sort

solution = Solution()
print(solution.convertToTitle([0,4,3,0,4]))


# toi uu
# return functools.reduce(lambda x, y: x ^ y, nums, 0)