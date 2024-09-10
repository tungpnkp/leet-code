# run time:
# memory:
class Solution:
    def action(self, nums: [int], original: int):
        while original <= nums[-1]:
            if original in nums:
                original = 2 * original
            else:
                break
        return original


solution = Solution()
print(solution.action([5,3,6,1,12], 3))
print(solution.action([2,7,9], 4))

