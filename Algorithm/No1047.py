# run time:
# memory:
class Solution:
    def action(self, s: str):
        tmp=[]
        for char in s:
            if not tmp or char != tmp[-1] :
                tmp.append(char)
            else:
                tmp.pop()
        return ''.join(tmp)


solution = Solution()
print(solution.action("abbaca"))
print(solution.action("azxxzy"))
# print(solution.action([1]))

