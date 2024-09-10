class Solution:
    def singleNumber(self, nums: []) -> int:
        tmps1 = {}
        for i in range(len(nums)):
            if nums[i] in tmps1:
                del tmps1[nums[i]]
            else:
                tmps1[nums[i]] = 1
        return next(iter(tmps1))

solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))


# toi uu
# return functools.reduce(lambda x, y: x ^ y, nums, 0)