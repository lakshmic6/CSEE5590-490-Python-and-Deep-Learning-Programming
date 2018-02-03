board_size = int(input("Enter Size of the board"))
board_size=board_size-1
print(" -- " * board_size)
print("|   " * (board_size + 1))
def print_horiz_line():
    print(" -- " * board_size)
def print_vert_line():
    print("|   " * (board_size + 1))
for index in range(board_size):
      print_horiz_line()
      print_vert_line()
print_horiz_line()