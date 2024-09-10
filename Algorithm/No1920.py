# run time:
# memory:
class Solution:
    def action(self, nums: []):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

solution = Solution()
print(solution.action([1,2,1]))
print(solution.action([1,3,2,1]))

