# run time:
# memory:
from audioop import reverse
from itertools import count


class Solution:
    def action(self, s: str):
        b = 0
        count = 0
        for c in s:
            # đếm toàn bộ phần tử b ở trước c
            if c == 'b':
                b += 1
            else:
                # Xóa a hoặc giữ lại a và xóa toàn bộ b ở trước c
                count = min(count + 1, b)
        return count

solution = Solution()
print(solution.action("ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"))
print(solution.action("bbaaaaabb"))

