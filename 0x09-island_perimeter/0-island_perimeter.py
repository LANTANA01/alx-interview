#!/usr/bin/python3
""" function that checks perimeter"""

def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    # Helper function to check if a cell is within grid boundaries
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check neighboring cells
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for x, y in neighbors:
                    if not is_valid(x, y) or grid[x][y] == 0:
                        perimeter += 1

    return perimeter
