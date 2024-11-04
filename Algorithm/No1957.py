# run time:
# memory:
class Solution:
    def action(self, s: str):
        fancyStr = s[0] + s[1]
        for i in range(2, len(s)):
            if fancyStr[-2] == s[i] and fancyStr[-1] == s[i]:
                continue
            fancyStr += s[i]
        return fancyStr


solution = Solution()
print(solution.action('leeetcode'))
print(solution.action('aaabaaaa'))
# print(solution.action([1]))

