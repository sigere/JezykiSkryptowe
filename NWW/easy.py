import sys


def nwd(x, y):
    while y != 0:
        tmp = y
        y = x % y
        x = tmp
    return x


if __name__ == "__main__":
    filename = sys.argv[1]

    file = open(filename, "r")
    data = file.read()
    pairs = data.split("\n")

    result = []
    for i in range(len(pairs)):
        pairs[i] = pairs[i].split(" ")
        a = int(pairs[i][0])
        b = int(pairs[i][1])
        n = nwd(a, b)
        result.append([n + 0.0, a * b / n])
    out = ''
    for i in range(len(result)):
        out += f'{pairs[i][0]}, {pairs[i][1]}, {result[i][0]}, {result[i][1]}\n'
    outfile = open(filename + ".out.txt", "w")
    outfile.write(out)
