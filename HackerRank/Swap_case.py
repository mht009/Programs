def swap_case(s):
    sw = []
    for i in s:
        if(i.islower() == True):
            sw.append(i.upper())

        elif(i.isupper()==True):
            sw.append(i.lower())

        else:
            sw.append(i)

    swmod = "".join(sw)

    return swmod

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)