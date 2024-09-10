# run time:
# memory:
class Solution:
    def action(self, s: str):
        if not s:
            return 0
        if s.replace(" ", "") == "":
            return 0
        return len([x for x in s.split(" ") if x != ""])


solution = Solution()
print(solution.action("Hello, my name is John"))

