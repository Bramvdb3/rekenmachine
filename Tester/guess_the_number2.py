import random

def raad(x):
    laag = 1
    hoog = x
    feedback = ""
    while feedback != 'c':
        guess = random.randint(laag, hoog)
        feedback = input(f"is {guess} te laag(l), te hoog(h) of correct(c)?   ")
        if feedback == 'h': 
            hoog = guess - 1
        elif feedback == 'l':
            laag = guess + 1
    print("ja je hebt het geraden aa kk daggoe")


def kees():
    hallo = ""
    if hallo == 7:
        print("het goede getal")
    elif hallo == 56:
        print("goedzo jongen")
    
        

kees()
            

       


       