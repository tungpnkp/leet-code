# run time:
# memory:
class Solution:
    def action(self, heights: []):
        expected=sorted(heights)
        count=0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count+=1
        return count

solution = Solution()
print(solution.action([1,1,4,2,1,3]))
print(solution.action([5,1,2,3,4]))

