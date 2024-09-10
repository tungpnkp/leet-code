# run time:
# memory:
class Solution:
    def action(self, dictionary: [], sentence: str):
        tmp = [' ' + x for x in sentence.split(' ')]
        tmp2 = []
        result = ''
        for string in sorted(dictionary):
            tmp2.append(' ' + string)
        for root in tmp2:
            for i in range(len(tmp)):
                if root in tmp[i]:
                    tmp[i] = root
        for x in tmp:
            result += x
        return result.replace(' ', '', 1)

solution = Solution()
print(solution.action(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(solution.action(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))

