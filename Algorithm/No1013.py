# run time:
# memory:
class Solution:
    def action(self, arr: []):
        sum_arr = sum(arr)
        if sum_arr % 3:
            return False
        sub_sum = sum_arr/3
        left = 0
        right = len(arr) - 1
        sum_left = arr[left]
        sum_right = arr[right]
        while left < right:
            if sum_left != sub_sum:
                left+=1
                sum_left += arr[left]
            if sum_right != sub_sum:
                right-=1
                sum_right += arr[right]
            if sum_left == sum_right and sum_left == sub_sum:
                break
        return (right - left) > 1

solution = Solution()
print(solution.action([0,2,1,-6,6,-7,9,1,2,0,1]))
print(solution.action([0,2,1,-6,6,7,9,-1,2,0,1]))
print(solution.action([3,3,6,5,-2,2,5,1,-9,4]))
print(solution.action([1,-1,1,-1]))

