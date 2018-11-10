from sys import argv

script, filename = argv

def main(file):
    line = file.readline()
    if line:
        print_line(line)
        main(file)


def print_line(line):
    lineStrip = line.strip()
    raw_bytes = lineStrip.encode('utf-8')
    stringBack = raw_bytes.decode('utf-8')
    print(raw_bytes, "<-->", stringBack)

file = open(filename)
main(file)

