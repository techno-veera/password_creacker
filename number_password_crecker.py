from random import *

count=0
user_pass = input("Enter your password:")

password = ['1','2','3','4','5','6','7','8','9','0'
]
guess = ""

while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0,9)]
        guess = str(guess_letter) + str(guess)
    print(guess)
    count+=1
    
print("Your password is :",guess)
print("No of password {} are checked for your password ".format(count))