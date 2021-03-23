import sys


def nwd(x, y):
    while y != 0:
        tmp = y
        y = x % y
        x = tmp
    return x


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = "input.txt"

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f'File "{filename}" not found! Exiting.')
        exit(1)

    data = file.read()
    pairs = data.split("\n")

    result = []
    try:
        for i in range(len(pairs)):
            pairs[i] = pairs[i].split(" ")
            if len(pairs[i]) != 2:
                raise IndexError
            a = int(pairs[i][0])
            b = int(pairs[i][1])
            n = nwd(a, b)
            result.append([n + 0.0, a * b / n])
    except IndexError:
        print(f"Invalid value on line {i+1}! Exiting.")
        exit(3)
    except ValueError:
        print(f"Invalid value on line {i+1}! Exiting.")
        exit(4)

    out = ''
    for i in range(len(result)):
        out += f'{pairs[i][0]}, {pairs[i][1]}, {result[i][0]}, {result[i][1]}\n'

    outfile = open(filename + ".out.txt", "w")
    outfile.write(out)
