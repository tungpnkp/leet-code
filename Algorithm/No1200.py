# run time:
# memory:
class Solution:
    def action(self, arr: []):
        arr = sorted(arr)
        min_diff = arr[1] - arr[0]
        data = []
        for i in range(1,len(arr)):
            if (arr[i] - arr[i-1]) == min_diff:
                data.append([arr[i-1],arr[i]])
            elif (arr[i] - arr[i-1]) < min_diff:
                data = [[arr[i-1],arr[i]]]
                min_diff = arr[i] - arr[i-1]
        return data


solution = Solution()
print(solution.action([4,2,1,3]))
print(solution.action([1,3,6,10,15]))
print(solution.action([3,8,-10,23,19,-4,-14,27]))
# print(solution.action([1]))

