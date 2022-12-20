# Program to take sample phishing mail and count the most coomonly occuring word
pmail = [
    "winlottery@indianloot.com",
    "luckywinner@lottery.com",
    "spinwheel@flipkart.com",
    "luckydeal@snapdeal.com" ,   
    "youarethewinner@myprize.com",
    "luckywinner@mymoney.com", 
    "Claimyourprize@money.com",
    "luckyjackpot@americanlottery.com"
    ]
myd = {}
for e in pmail :
    z = e.split('@')
    for w in z :
        if w not in myd:
            myd[w] = 1
        else:
            myd[w] += 1

maxw = max(myd, key = myd.get)
print("Most common Occuring Word is : ", maxw)
