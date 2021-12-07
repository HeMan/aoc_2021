def tochars(line):
    return list(map(int, list(line.rstrip())))


def mostcommon(numberoflines, numberofbits):
    if numberoflines / 2 > numberofbits:
        return "0"
    else:
        return "1"


def part1(filename):
    numberofbits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numberoflines = 0
    with open(filename) as f:
        for line in f:
            if line:
                numberofbits = [sum(x) for x in zip(tochars(line), numberofbits)]
                numberoflines += 1

        gamma = int(("".join([mostcommon(numberoflines, x) for x in numberofbits])), 2)
        epsilon = int(
            (
                "".join(
                    [mostcommon(numberoflines, numberoflines - x) for x in numberofbits]
                )
            ),
            2,
        )

        print(gamma * epsilon)


if __name__ == "__main__":
    part1("input.txt")
