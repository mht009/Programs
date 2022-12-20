string = "Mohit"

subStrings = []

for i in range(len(string)):
    for j in range(i+1, len(string) +1):
        subStrings.append(string[i:j])

#         # Using list comprehension + string slicing
# res = [test_str[i: j] for i in range(len(test_str))
# 		for j in range(i + 1, len(test_str) + 1)]

print(subStrings)