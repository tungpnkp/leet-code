# run time:
# memory:
class Solution:
    def action(self, arr1: [], arr2: []):
        arr2_swap =  {value: index for index, value in enumerate(arr2)}
        array_len = len(arr2)
        tmp=sorted(arr1, key=lambda x: array_len+x if x not in arr2_swap else arr2_swap[x])
        return tmp


solution = Solution()
print(solution.action([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(solution.action([28,6,22,8,44,17], [22,28,8,6]))
# print(solution.action([1]))

