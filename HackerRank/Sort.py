lst = []
sortlst = []
for i in range(1,11):
    lst.append(i)

print("Original list:\n",lst)
for i in lst:
    for j in lst:
        if(i+j==12):
            if([j,i] not in sortlst):
                sortlst.append([i,j])

print("Set of number whose sum equals 12: \n",sortlst)