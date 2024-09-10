# run time:
# memory:
class Solution:
    def action(self, n:int):
        tmp = []
        for i in range(1,n+1):
            if i%15==0:
                tmp.append("FizzBuzz")
            elif i%3==0:
                tmp.append("Fizz")
            elif i%5==0:
                tmp.append("Buzz")
            else:
                tmp.append(str(i))
        return tmp

solution = Solution()
print(solution.action(3))
print(solution.action(15))

