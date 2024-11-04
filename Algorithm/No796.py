# run time:
# memory:
class Solution:
    def action(self, s: str, goal: str):
        if len(s) != len(goal):
            return False
        tmp = s
        for i in range(len(s)):
            if tmp == goal:
                return True
            tmp = tmp[1:] + tmp[0]
        return False


solution = Solution()
print(solution.action('abcde', 'cdeab'))
print(solution.action('abcde', 'abced'))

