# run time:
# memory:
class Solution:
    def action(self, text: str):
        tmp = {
            "a": 0,
            "b": 0,
            "l": 0,
            "n": 0,
            "o": 0
        }
        for char in text:
            if char in tmp:
                tmp[char] += 1
        tmp['o'] = tmp['o'] // 2
        tmp['l'] = tmp['l'] // 2

        return min(tmp.values())


solution = Solution()
print(solution.action("nlaebolko"))
print(solution.action("loonbalxballpoon"))
# print(solution.action([1]))

