# Finite generators can be converted into lists by passing them as an arguments to the list function

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

''' Using generators results in improved performance, which is the result of lazy (on demand) gerneration of values,
    which translates to ;ower memory usage. Furthermore, we don't need to wait until all the elements have been generated before we start to use them.
'''
print("-------------------------------------------------------------")

# Example
def make_word():
    word = ""
    for ch in "spam" :
        word += ch 
        yield word

print(list(make_word()))
