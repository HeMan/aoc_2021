def part2(filename):
    last = (10000, 10000, 10000)
    count = 0
    with open(filename) as f:
        for line in f:
            value = last
            last = (last[1], last[2], int(line))
            if sum(value) < sum(last):
                count += 1

    print(count)

if __name__ == "__main__":
    part2("input.txt")
