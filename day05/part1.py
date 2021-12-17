import gc


def part1(filename):
    board = {}
    count = 0
    with open(filename) as f:
        for line in f:
            (p1, p2) = [
                list(map(int, x.rstrip().split(","))) for x in line.rstrip().split("->")
            ]
            if p1[0] == p2[0] or p1[1] == p2[1]:
                lowx = min(p1[0], p2[0])
                highx = max(p1[0], p2[0])
                lowy = min(p1[1], p2[1])
                highy = max(p1[1], p2[1])
                if board.get((lowy, highy)):
                    board[(lowy, highy)].append((lowx, highx))
                else:
                    board[(lowy, highy)] = [(lowx, highx)]

            gc.collect()

        for i in range(1000):
            dataline = dict(filter(lambda y: y[0][0] <= i <= y[0][1], board.items()))
            if len(dataline) >= 1:
                values = [item for sublist in dataline.values() for item in sublist]
                vmin = min([min(v[0], v[1]) for v in values])
                vmax = max([max(v[0], v[1]) for v in values])
                for j in range(vmin, vmax):
                    if len(list(filter(lambda x: x[0] <= j <= x[1], values))) >= 2:
                        count += 1

        print(count)


if __name__ == "__main__":
    part1("input.txt")
