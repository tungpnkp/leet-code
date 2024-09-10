# run time:
# memory:
class Solution:
    def action(self, nums: []):
        tmp = {
            0: 0,
            1: 0,
            2: 0
        }
        for num in nums:
            tmp[num] += 1
        nums = []
        for key, value in tmp.items():
            nums += value*[key]
        return nums

solution = Solution()
print(solution.action([2,0,2,1,1,0]))
print(solution.action([2,0,1]))

