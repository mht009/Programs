# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inp = input()
ele = (inp.split())
# print(ele)

intlst = [int(i) for i in ele]
# print(intlst)
t = tuple(intlst)
print(t)
print(hash(t))