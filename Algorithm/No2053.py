# run time:
# memory:
from itertools import count
class Solution:
    def action(self, arr: [], k):
        my_dict = {}
        for c in arr:
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        for key, val in my_dict.items():
            if val == 1:
                k-=1
            if k == 0:
                return key
        return ""

solution = Solution()
print(solution.action(["d","b","c","b","c","a"], 2))
print(solution.action(["aaa","aa","a"], 1))

