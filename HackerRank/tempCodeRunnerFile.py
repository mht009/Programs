import re

def replace(text, N):
    reptext = text
    for i in range (N):
        reptext = re.sub("\s&&\s", " and ", reptext)
        reptext = re.sub("\s[|][|]\s", " or ", reptext)
    # reptext = re.sub("\s&&\s", " and ", reptext)


    print(reptext)

def main():
    lines = int(input())
    for i in range(lines):
        line = input()
        replace(line, lines)



main()