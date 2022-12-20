if __name__ == '__main__':
    s = input()
    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if(i.isalpha()==True):
            alpha = True
        if(i.isalnum()==True):
            alphanum = True
        if(i.isdigit()==True):
            digit = True
        if(i.islower()==True):
            lower = True
        if(i.isupper()==True):
            upper = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)