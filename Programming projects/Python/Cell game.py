# -1 to start the simulation
# 0,0 is the top left corner
def format(cells):
    for row in cells:     # Gosper Glider
        for cell in row:  # □ □ ■
            if cell == 0: # ■ □ ■
                cell = "□"# □ ■ ■
            else:
                cell = "■"
            print(cell, end=" ")
        print()

def count_neighbors(grid, row, col): # This function and the update_cells function were made by AI
    count = 0                        # Sorry
    rows = len(grid)
    cols = len(grid[0])
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                count += 1
    return count

def update_cells(cells):
    new_cells = [[0] * len(cells[0]) for _ in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            neighbors = count_neighbors(cells, i, j)
            if cells[i][j] == 1 and (neighbors == 2 or neighbors == 3):
                new_cells[i][j] = 1
            elif cells[i][j] == 0 and neighbors == 3:
                new_cells[i][j] = 1
    return new_cells

board_height = int(input("Enter height of board: "))
board_length = int(input("Enter length of board: "))
cells = [[0] * board_length for _ in range(board_height)]

while True:
    startX = int(input("Enter X: "))
    if startX == -1:
        break
    startY = int(input("Enter Y: "))

    if startX >= board_length or startY >= board_height:
        print("This is not a correct coordinate")
    else:
        cells[startY][startX] = int(not cells[startY][startX])
        format(cells)
generations = int(input("Enter the number of generations you want: "))
for _ in range(generations):
    cells = update_cells(cells)
    format(cells)
