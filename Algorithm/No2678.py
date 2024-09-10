# run time:
# memory:
class Solution:
    def action(self, details: []):
        return len([x[11:13] for x in details if x[11:13] > '60'])

solution = Solution()
print(solution.action(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(solution.action(["1313579440F2036","2921522980M5644"]))

