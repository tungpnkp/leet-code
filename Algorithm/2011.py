# run time:
# memory:
class Solution:
    def action(self, operations: []):
        base = 0
        for i in operations:
            if "--" in i:
                base -= 1
            else:
                base += 1
        return base

solution = Solution()
print(solution.action(["--X","X++","X++"]))
print(solution.action(["++X","++X","X++"]))
# print(solution.action([1,2,3]))
