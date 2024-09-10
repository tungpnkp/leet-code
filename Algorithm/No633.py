# run time:
# memory:
class Solution:
    def action(self,c: int):
        a = 0
        end = c // 2 + 1
        while a < end:
            first = a * a
            if first > c:
                return False
            b = sqrt(c - first)
            if b==int(b):
                return True
        return False

solution = Solution()
print(solution.action(5))
print(solution.action(3))

