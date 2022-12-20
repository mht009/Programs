

# Complete the solve function below.
def solve(s):
    indexlst = []
    for i in range(len(s)):
        if(s[i] == ' '):
            indexlst.append(i)

    items = s.split()
    items = [i.capitalize() for i in items]

    string = "".join(items)
    lst = [i for i in string]
    # print(lst)

    for i in indexlst:
        lst.insert(i, " ")
    
    # print(lst)
    modString = "".join(lst)

    # print(modString)
    return modString
    

if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)
