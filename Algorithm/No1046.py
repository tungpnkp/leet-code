# run time:
# memory:
class Solution:
    def action(self, stones: []):
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        while len(stones) > 1:
            max_1st = stones.pop()
            max_2nd = stones.pop()
            if max_1st > max_2nd:
                stones.append(max_1st-max_2nd)
                stones.sort()

        return 0 if not stones else stones[0]


solution = Solution()
print(solution.action([2,7,4,1,8,1]))
print(solution.action([2,2]))
# print(solution.action([1]))

