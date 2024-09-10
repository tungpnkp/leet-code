# run time:
# memory:
class Solution:
    def action(self, distance: [], start: int, destination: int):
        dis = 0
        if start > destination:
            dis=min(sum(distance[destination:start]), sum(distance[0:destination]) + sum(distance[start:]))
        else:
            dis=min(sum(distance[start:destination]), sum(distance[0:start]) + sum(distance[destination:]))
        return dis


solution = Solution()
print(solution.action([1,2,3,4], 0,1))
print(solution.action([1,2,3,4], 0,3))
# print(solution.action([1]))

