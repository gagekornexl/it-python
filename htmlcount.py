import os

from banner import banner
banner("HTML TAG COUNTER","Gage")


def load(filename):
    data = []
    print(f"..... loading from {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def tags_in(line):
    count = 0
    previous_char = None
    for char in line:
        if char != "/" and previous_char == "<":
            count += 1
        previous_char = char
    return count

def main():
    print("Welcome to the HTML tag counter")
    filename = input("Please enter the name of the HTML file:")
    data = load(filename)
    count = 0
    for line in data:
        count += tags_in(line)

    print(count)





main()