import random

users=list()

def add_user(x):
    print("-"*30)
    print("Welcome to add user screen")
    add=input("Please enter a user  name: ")
    users.append(add)
    input("İf you want to continiue  press a button")


def show_user(x):
    count = 1
    print("-"*30)
    for i in x:
        print(str(count)+"-User name:",i)
        count+=1
        print("-"*30)
    input("İf you want to continiue  press a button")


def pic(x):
    print("-"*30)
    count=1
    pic_person=int(input("How man people do you want to pick: "))
    pic_random=random.sample(x,pic_person)

    for i in pic_random:
        print(str(count)+"-User name:",i)
        count+=1
    print("-"*30)
    input("İf you want to continiue  press a button")


def shake(x):
    count=1
    random.shuffle(x)
    for i in x:
        print(str(count)+"-User name:",i)
        count+=1
    input("İf you want to continiue  press a button")    
    


while True:
    print("***Welcome to Draw Application***")
    action = int(input("1-Add User\n2-Show User\n3-Shake User\n4-Pic Random User\n"))

    if action==1:
        add_user(users)
    elif action==2:
        show_user(users)
    elif action==3:
        shake(users)
    elif action==4:
        pic(users)
    else:
        print("Please pic anyone of the actions!!!!!!!!")    
