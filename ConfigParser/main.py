import configparser as CP
from pathlib import Path

if __name__ == '__main__':

    filename = 'input.rc'
    if not Path(filename).is_file():
        print(f"file '{filename}' not found")
        exit()

    rd = CP.ConfigParser()
    rd.read('input.rc')
    result = []
    for i in rd.sections():
        tmp = 1
        for j in range(1, len(rd.items(i))):
            tmp *= float(rd.items(i)[j][1])
        sign = 1 if tmp > 0 else -1
        result.append(abs(tmp) ** (1. / 3) * sign)

    out = open("output.txt", "w")
    out.write(f'Pomiar\t\t srednia geom.\n')
    for i in range(len(result)):
        out.write(f'{rd.sections()[i]}:\t\t {result[i]}\n')
