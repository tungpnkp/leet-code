# run time:
# memory:
class Solution:
    def action(self, hand: [], groupSize: int):
        if len(hand)%groupSize !=0:
            return False
        while len(hand) != 0:
            min_num = min(hand)
            hand.remove(min_num)
            for j in range(1,groupSize):
                if (min_num+j) in hand:
                    hand.remove(min_num+j)
                else:
                    return False
        return True

solution = Solution()
print(solution.action([1,2,3,6,2,3,4,7,8], 3))
print(solution.action([1,2,3,4,5], 4))
print(solution.action([1,2,3,4,5,6], 2))
print(solution.action([2,1], 2))

