# run time: 69%
# memory: 75%
class Solution:
    def action(self, words:[]):
        common_chars = list(words[0])
        for word in words[1:]:
            new_common_chars = []
            for char in common_chars:
                if char in word:
                    new_common_chars.append(char)
                    word = word.replace(char, '', 1)
            common_chars = new_common_chars
        return common_chars
solution = Solution()
print(solution.action(["bella","label","roller"]))
print(solution.action(["cool","lock","cook"]))

