def split_and_join(line):
    lst = line.split()
    joinedline = "-".join(lst)
    return joinedline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)