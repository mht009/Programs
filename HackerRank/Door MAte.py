inp = input()
lst = inp.split()

N = int(lst[0])
M = int(lst[1])
k = 3 #space occupying .|.
l = 1 #no of times .|. to be printed 
p = int((M-k)/2)

w = (M-7)//2

for i in range(N//2):
    print(p*"-" + l*".|." + p*"-")
    p = p-3
    l = l+2

print(w*"-"+"WELCOME"+w*"-")
p = 3
l = l-2
for i in range(N//2):
    print(p*"-" + l*".|." + p*"-")
    p = p+3
    l = l-2