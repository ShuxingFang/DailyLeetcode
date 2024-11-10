from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        ans = 0

        for arr in grid:
            row_dict[tuple(arr)] += 1

        for i in range(len(grid)):
            col = []
            for arr in grid:
                col.append(arr[i])
            col_dict[tuple(col)] += 1


        for key in row_dict:
            if key in col_dict:
                ans += row_dict[key] * col_dict[key]


        return ans




grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
solution = Solution()
print(solution.equalPairs(grid))
