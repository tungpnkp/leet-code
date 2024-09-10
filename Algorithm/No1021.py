# run time:
# memory:
class Solution:
    def action(self, s: str):
        count = 0
        tmp = ''
        for char in s:
            if char == "(":
                count+=1
            if count != 1:
                tmp +=char
            if char == ")" :
                count-=1
        return tmp

solution = Solution()
print(solution.action("(()())(())"))
print(solution.action("(()())(())(()(()))"))

