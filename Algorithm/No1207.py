# run time:
# memory:
class Solution:
    def action(self, arr: []):
        tmp = {}
        for x in arr:
            if x in tmp:
                tmp[x] += 1
            else:
                tmp[x] = 1
        return len(tmp) == len(set(tmp.values()))


solution = Solution()
print(solution.action([1,2,2,1,1,3]))
print(solution.action([1,2]))
print(solution.action([-3,0,1,-3,1,1,1,-3,10,0]))
# print(solution.action([1]))

