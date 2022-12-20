def print_formatted(number):
    
        for i in range(1, number+1):
            print("{:>3}  {:>3}  {:>3}  {:>6}".format(str(i), oct(i).replace("0o",""), hex(i).upper().replace("0X",""),  bin(i).replace("0b","")))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)