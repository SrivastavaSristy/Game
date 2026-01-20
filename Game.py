from authen import auth_user,login
from Score import Scoreget

auth = []
name = input("Enter your name")
coins = int(input("Enter your coins"))
level = int(input("Enter your level"))
db = {}
print(auth_user(name,coins,level,db))
print(login(name,coins,level,db))

failure_count = 0
for i in range (0,3):
    score = Scoreget()
    if score>=60:
        level+=1
        coins+=100
        print("you passed this level")
        break
    else:
        failure_count+=1

if failure_count ==3:
    level-=1
    coins-=100
    print("better luck next time")
