# run time:
# memory:
class Solution:
    def action(self, s: [], c: str):
        s = list(s)
        tmp=[]
        c_index_1 = s.index(c)
        c_index_2 = 0
        for i in range(len(s)):
            if s[i] == c and i > c_index_1:
                c_index_2=c_index_1
            tmp.append(abs(min(c_index_1-i, i-c_index_2)))
        return tmp

solution = Solution()
# print(solution.action("loveleetcode",  "e"))
print(solution.action("etcode",  "e"))

