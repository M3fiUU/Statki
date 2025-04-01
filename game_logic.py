def can_place_ship(board, x, y, size, direction):
    if direction == "H":
        if x + size > 10:
            return False
        for i in range(size):
            if board[y][x + i] != "~":
                return False
    else:
        if y + size > 10:
            return False
        for i in range(size):
            if board[y + i][x] != "~":
                return False
    return True

def check_hit(board, x, y):
    if board[y][x] == "S":
        board[y][x] = "X"
        return True
    elif board[y][x] == "~":
        board[y][x] = "O"
    return False

def all_ships_sunk(board):
    for row in board:
        if "S" in row:
            return False
    return True

def is_ship_sunk(ships, board, x, y):
    for ship in ships:
        if (x, y) in ship:
            for sx, sy in ship:
                if board[sy][sx] == "S":
                    return False
            return True
    return False

def create_empty_board():
    return [["~" for _ in range(10)] for _ in range(10)]

def place_ship(board, x, y, size, direction):
    coords = []
    if direction == "H":
        if x + size > 10:
            return None
        for i in range(size):
            if board[y][x + i] != "~":
                return None
            coords.append((y, x + i))
    else:  # direction == "V"
        if y + size > 10:
            return None
        for i in range(size):
            if board[y + i][x] != "~":
                return None
            coords.append((y + i, x))

    for cy, cx in coords:
        board[cy][cx] = "S"
    return coords

