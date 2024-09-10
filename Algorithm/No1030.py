# run time:
# memory:
class Solution:
    def action(self, rows: int, cols: int, rCenter: int, cCenter: int):
        all_cells = [[r, c] for r in range(rows) for c in range(cols)]
        all_cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return all_cells

solution = Solution()
print(solution.action(1,2,0,0))

