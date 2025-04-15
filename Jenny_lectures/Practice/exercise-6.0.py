# paly with games 
import random
# select = input("what you want(HEAD/TAILS):")
toss = ["HEAD", "TAILS"]

options = random.choice(toss)

if options == 'HEAD':
    print("Won this toss")
else:
    print("Loos the toss")