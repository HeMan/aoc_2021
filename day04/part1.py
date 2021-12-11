import gc

boards = []


def readboard(filename):
    emptyline = filename.readline()
    if not emptyline:
        return None

    board = [
        [int(v) for v in filename.readline().rstrip().split()],
        [int(v) for v in filename.readline().rstrip().split()],
        [int(v) for v in filename.readline().rstrip().split()],
        [int(v) for v in filename.readline().rstrip().split()],
        [int(v) for v in filename.readline().rstrip().split()],
    ]

    return board


def check_board(board):
    for line in board:
        if sum(line) == 0:
            return True
    for col in range(5):
        if sum([board[ln][col] for ln in range(5)]) == 0:
            return True
    return False


def mark(numbers):
    for number in numbers:
        for board in boards:
            for line in board:
                if number in line:
                    line[line.index(number)] = 0
                    if check_board(board):
                        print(sum([i for s in board for i in s]) * number)
                        return True
    return False


def part1(filename):
    with open(filename) as f:
        drawnumbers = [int(v) for v in f.readline().rstrip().split(",")]
        while True:
            board = readboard(f)
            if not board:
                break
            boards.append(board)
            gc.collect()
    mark(drawnumbers)


if __name__ == "__main__":
    part1("input.txt")
