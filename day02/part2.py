def part2(filename):
    with open(filename) as f:
        total_down, total_distance, aim = (0,0,0)
        for line in f:
            direction, dstr = line.split()
            distance = int(dstr)
            if direction == "down":
                aim += distance
            elif direction == "up":
                aim -= distance
            elif direction == "forward":
                total_distance += distance
                total_down += aim * distance

    print(total_down * total_distance)

if __name__ == "__main__":
    part2("input.txt")
