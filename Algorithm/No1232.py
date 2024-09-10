# run time:
# memory:
class Solution:
    def action(self, coordinates: []):
        if len(coordinates) == 2:
            return True
        vector1 = [coordinates[0][0]-coordinates[1][0], coordinates[0][1]-coordinates[1][1]]

        for i in range(2, len(coordinates)):
            if vector1[0] * (coordinates[i][1] - coordinates[0][1]) != vector1[1]*(coordinates[i][0] - coordinates[0][0]):
                return False
        return True


solution = Solution()
print(solution.action([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(solution.action([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))

