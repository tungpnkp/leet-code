# run time: 69%
# memory: 75%
class Solution:
    def action(self, s:str):
        tmp = []
        count=0
        for char in s:
            if char in tmp:
                tmp.remove(char)
                count+=2
            else:
                tmp.append(char)
        return count + 1 if tmp else count

solution = Solution()
print(solution.action('Aa'))
print(solution.action('aaa'))
print(solution.action('a'))
print(solution.action('abccccdd'))

