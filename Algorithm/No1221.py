# run time:
# memory:
class Solution:
    def action(self, s: str):
        count = 0
        result = 0
        for char in s:
            if char=="R":
                count-=1
            else:
                count+=1
            if count == 0:
                result+=1
        return result


solution = Solution()
print(solution.action("RLRRLLRLRL"))
print(solution.action("RLRRRLLRLL"))
print(solution.action("LLLLRRRR"))

