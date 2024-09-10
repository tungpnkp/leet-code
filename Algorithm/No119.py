class Solution:
    def generate(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        numIndx = rowIndex + 1
        list1 = []
        list1.append([1])
        list1.append([1, 1])
        for i in range(2, numIndx):
            tmp = []
            tmp.append(1)
            for j in range(1, i):
                tmp.append(list1[i - 1][j - 1] + list1[i - 1][j])
            tmp.append(1)
            list1.append(tmp)
        return list1[-1]

solution = Solution()
print(solution.generate(0))
