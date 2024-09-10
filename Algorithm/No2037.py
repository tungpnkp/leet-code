# run time:
# memory:
class Solution:
    def action(self, seats: [], students: []):
        seats = sorted(seats)
        students = sorted(students)
        tmp = 0
        for i in range(len(students)):
            tmp += abs(seats[i] - students[i])
        return tmp


solution = Solution()
print(solution.action([3,1,5], [2,7,4]))
print(solution.action([4,1,5,9], [1,3,2,6]))
# print(solution.action([1]))

