# run time:
# memory:
class Solution:
    def action(self, s: str):
        count = 0
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                count += 1
            i += 2
        return count

solution = Solution()
print(solution.action('1001')) #2
print(solution.action('0000')) #0

