def merge_the_tools(string, k):
    n = len(string)
    iter = n/k
    start = 0
    for i in range(iter):
        substring = string[start: (start+k)]
        start += k
        # print(substring)
        
        sublist = list(substring)
        sublist2 = []

        for i in sublist:
            if i not in sublist2:
                sublist2.append(i)
    
        # print(str(sublist2))\
        if(len(sublist2) == 1):
            print((sublist2[0]))
            
        else:
            reqString = ''.join(sublist2)
            print(reqString)

if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)