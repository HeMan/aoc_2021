import gc

boards = []
winningboards = []
winningboard = 0


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
    global winningboard
    for number in numbers:
        for boardnr in range(len(boards)):
            if boardnr in winningboards:
                continue
            for line in boards[boardnr]:
                if number in line:
                    line[line.index(number)] = 0
                    if check_board(boards[boardnr]):
                        winningboards.append(boardnr)
                        winningboard = (
                            sum([i for s in boards[boardnr] for i in s]) * number
                        )
                        gc.collect()


def part2(filename):
    with open(filename) as f:
        drawnumbers = [int(v) for v in f.readline().rstrip().split(",")]
        while True:
            board = readboard(f)
            if not board:
                break
            boards.append(board)
            gc.collect()
    mark(drawnumbers)

    print(winningboard)


if __name__ == "__main__":
    part2("input.txt")
