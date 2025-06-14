def flood_fill(grid, x, y, color):
    n = len(grid)
    m = len(grid[0])
    if grid[x][y] != 0:
        return

    stack = [(x, y)]
    while stack:
        i, j = stack.pop()
        if 0 <= i < n and 0 <= j < m and grid[i][j] == 0:
            grid[i][j] = color
            stack.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

def fill_all_regions(grid, start_x, start_y):
    n = len(grid)
    m = len(grid[0])
    color = 2

    # Começa da célula inicial
    if grid[start_x][start_y] == 0:
        flood_fill(grid, start_x, start_y, color)
        color += 1

    # Continua o preenchimento para as demais regiões
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                flood_fill(grid, i, j, color)
                color += 1

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))



# Sua entrada
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0]
]

start_x = 0
start_y = 0

fill_all_regions(grid, start_x, start_y)
print_grid(grid)
