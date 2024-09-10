# run time:
# memory:
class Solution:
    def action(self, position: []):
        tmp = {
            0:0,
            1:0
        }
        for x in position:
            tmp[x%2] += 1
        return min(tmp[0], tmp[1])


solution = Solution()
print(solution.action([6,4,7,8,2,10,2,7,9,7]))
# print(solution.action([1,2,3]))
# print(solution.action([1,1000000000]))

