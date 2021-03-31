from pathlib import Path
import math

if __name__ == '__main__':
    filename = 'input.txt'
    if not Path(filename).is_file():
        print(f"file '{filename}' not found")
        exit()
    with open(filename) as file:
        text = file.read()
    text = text.splitlines()
    headers = text[0].split(",")
    data = []
    validLines = 0
    for i in range(1, len(text)):
        text[i] = text[i].split(",")
        line = []
        try:
            if len(text) < 4:
                raise SyntaxError
            if not len(text[i][0]):
                raise SyntaxError
            line = [
                text[i][0],
                int(text[i][1]),
                int(text[i][2]),
                int(text[i][3])
            ]
        except SyntaxError:
            continue
        except ValueError:
            continue
        data.append(line)
        validLines += 1

    headers.append("y")
    for i in range(len(data)):
        value = math.e**(-((data[i][1]-data[i][2])/data[i][3])**2)
        data[i].append(value.__str__())

    with open("output.txt", "w") as file:
        for header in headers:
            file.write(f'{header},')
        file.write(f'\n')
        for line in data:
            for col in line:
                file.write(f'{col},')
            file.write('\n')

    print(data)
    print(validLines)
