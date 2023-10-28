# BEGIN

from typing import List

n, m = 3, 3
heights = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]

def calculate_max_water_collected(n: int, m: int, heights: List[List[int]]) -> float:
    water = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            lowest_adjacent_elevation = float('inf')
            lowest_adjacent_count = 0
            if i > 0 and heights[i-1][j] < heights[i][j]:
                lowest_adjacent_elevation = min(lowest_adjacent_elevation, heights[i-1][j])
            if i < n-1 and heights[i+1][j] < heights[i][j]:
                lowest_adjacent_elevation = min(lowest_adjacent_elevation, heights[i+1][j])
            if j > 0 and heights[i][j-1] < heights[i][j]:
                lowest_adjacent_elevation = min(lowest_adjacent_elevation, heights[i][j-1])
            if j < m-1 and heights[i][j+1] < heights[i][j]:
                lowest_adjacent_elevation = min(lowest_adjacent_elevation, heights[i][j+1])
            if i > 0 and heights[i-1][j] == lowest_adjacent_elevation:
                lowest_adjacent_count += 1
            if i < n-1 and heights[i+1][j] == lowest_adjacent_elevation:
                lowest_adjacent_count += 1
            if j > 0 and heights[i][j-1] == lowest_adjacent_elevation:
                lowest_adjacent_count += 1
            if j < m-1 and heights[i][j+1] == lowest_adjacent_elevation:
                lowest_adjacent_count += 1
            if lowest_adjacent_elevation < float('inf'):
                water_flow = water[i][j] / lowest_adjacent_count
                if i > 0 and heights[i-1][j] == lowest_adjacent_elevation:
                    water[i-1][j] += water_flow
                if i < n-1 and heights[i+1][j] == lowest_adjacent_elevation:
                    water[i+1][j] += water_flow
                if j > 0 and heights[i][j-1] == lowest_adjacent_elevation:
                    water[i][j-1] += water_flow
                if j < m-1 and heights[i][j+1] == lowest_adjacent_elevation:
                    water[i][j+1] += water_flow
                water[i][j] -= water_flow * lowest_adjacent_count
    total_water = sum(sum(row) for row in water)
    return total_water

# Sample Output
print(calculate_max_water_collected(n, m, heights))
# END
