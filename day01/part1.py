def part1(filename):
    last = 100000
    count = 0
    with open(filename) as f:
        for line in f:
            value = int(line)
            if value > last:
                count += 1
            last = value

    print(count)

if __name__ == "__main__":
    part1("input.txt")
