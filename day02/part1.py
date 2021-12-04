def part1(filename):
    with open(filename) as f:
        total_down, total_distance = (0,0)
        for line in f:
            direction, distance = line.split()
            if direction == "down":
                total_down += int(distance)
            elif direction == "up":
                total_down -= int(distance)
            elif direction == "forward":
                total_distance += int(distance)

    print(total_down * total_distance)

if __name__ == "__main__":
    part1("input.txt")
