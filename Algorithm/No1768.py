# run time:
# memory:
class Solution:
    def action(self, word1: str, word2: str):
        string=''
        w1 = list(word1)
        w2 = list(word2)
        len1 = len(w1)
        len2 = len(w2)
        for i in range(min(len1, len2)):
            string += (w1[i] + w2[i])
        if len1 != len2:
            string += ''.join(w1[len2-1:] if len1 > len2 else w2[len1-1:])
        return string


solution = Solution()
# print(solution.action("abc", "pqr"))
print(solution.action("abcd", "pq"))

