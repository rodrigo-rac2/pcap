def check_unique(nums):
    seen = set()
    for num in nums:
        if num != 0 and num in seen:
            return False
        seen.add(num)
    return True

def check_row(row):
    return check_unique(row)

def check_col(grid, col):
    return check_unique([row[col] for row in grid])

def check_tiles(grid):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_unique([grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                return False
    return True

if __name__ == "__main__":
    grid = []
    print("Enter the sudoku grid (9x9) row by row (9 rows) or X to exit:")
    for i in range(9):
        row = input(f"row number {i+1}: ")
        if row == 'X':
            print("Exiting...")
            break
        elif not row.isdigit() or len(row) != 9:
            print("Invalid row, only a total of 9 numbers are allowed")
            break
        else:
            grid.append([int(x) for x in row])
    else:
        if len(grid) != 9:
            print("Invalid grid, only a total of 9 rows are allowed")
        else:
            if all(check_row(row) for row in grid) and all(check_col(grid, i) for i in range(9)) and check_tiles(grid):
                print("Yes")
            else:
                print("No")


# def check_row(row):
#     num_list = []
#     for number in row:
#         if number in num_list:
#             return False
#         num_list.append(number)
#     return True

# def check_col(grid, col):
#     num_list = []
#     for row in grid:
#         if row[col] in num_list:
#             return False
#         num_list.append(row[col])
#     return True

# def check_tiles(grid):
#     for i in range(9):
#         num_list = []
#         if i == 0:
#             for y in range(3):
#                 for x in range(3):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 1:
#             for y in range(3,6):
#                 for x in range(3):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 2:
#             for y in range(6,9):
#                 for x in range(3):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 3:
#             for y in range(3):
#                 for x in range(3,6):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 4:
#             for y in range(3,6):
#                 for x in range(3,6):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 5:
#             for y in range(6,9):
#                 for x in range(3,6):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 6:
#             for y in range(3):
#                 for x in range(6,9):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 7:
#             for y in range(3,6):
#                 for x in range(6,9):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
#         elif i == 8:
#             for y in range(6,9):
#                 for x in range(6,9):
#                     if grid[y][x] in num_list:
#                         return False
#                     num_list.append(grid[y][x])
    
#     return True


# if __name__ == "__main__":
#     grid = []
#     exit = False
#     print("Enter the sudoku grid (9x9) row by row (9 rows) or X to exit:")
#     for i in range(9):
#         row = input(f"row number {i+1}: ")
#         if row == 'X':
#             exit = True
#             break
#         elif not row.isnumeric() or len(row) != 9:
#             print("Invalid row, only a total of 9 numbers are allowed")
#             exit = True
#             break
#         else:
#             grid.append([int(x) for x in row])
#     if exit:
#         print("Exiting...")
#     elif len(grid) != 9:
#         print("Invalid grid, only a total of 9 rows are allowed")
#     else: 
#         for i in range(9):
#             if not check_row(grid[i]):
#                 print("No")
#                 exit = True
#                 break
#         if not exit:
#             for i in range(9):
#                 if not check_col(grid, i):
#                     print("No")
#                     exit = True
#                     break
#         if not exit: 
#             if not check_tiles(grid):
#                 print("No")
#             else: print("Yes")
