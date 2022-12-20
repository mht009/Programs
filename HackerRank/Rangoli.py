def print_rangoli(size):
    alphabets = []
    for i in range(65, 91):
        alphabets.append(chr(i).lower())

    print(alphabets)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)