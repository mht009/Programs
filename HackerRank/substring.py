def count_substring(string, sub_string):
    # print(string)
    # print(sub_string)
    num = i = 0
    n = len(string)
    m = len(sub_string)
    for j in range(0, n):
        
        if(string[i:i+m]==sub_string):
            # print(string[i:i+3])
            num += 1
            string = string[i+1:]
            i = 0
        #     print(string)
        # print(string)
        i+=1
    return num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)