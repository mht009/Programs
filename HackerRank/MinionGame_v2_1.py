# Ye mera code nahi hai

def minion_game(string):
    l = len(string)
    vowels = set("AEIOU")
    v_sum = c_sum = 0;    
    for i in range(l):
        if string[i] in vowels:
            v_sum += l - i;
        else:
            c_sum += l - i;
    if (v_sum == c_sum):
        print("Draw")
    else:
        print(f"Kevin {v_sum}") if v_sum > c_sum else print(f"Stuart {c_sum}")




if __name__ == '__main__':
    s = input()
    minion_game(s)