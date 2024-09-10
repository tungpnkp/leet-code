# run time:
# memory:
class Solution:
    def action(self, points: {}):
        if points[0][0] == points[1][0] and points[1][0] == points[2][0]:
            if points[0][1] == points[1][1]:
                return False
            else:
                return True

        return points[2][0] * ((points[0][1] - points[1][1]) / (points[0][0] - points[1][0])) + ((points[0][0]*points[1][1] - points[1][0]*points[0][1])/(points[0][0] - points[1][0])) != points[2][1]


solution = Solution()
print(solution.action([[1,1],[2,3],[3,2]]))
print(solution.action([[1,1],[2,2],[3,3]]))

