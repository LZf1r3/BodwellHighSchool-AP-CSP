def code_1():
    import random
    num1=random.randint(1,5)
    num2=random.randint(1,5)

    #while the first guess is incorrect, keep asking the user to guess again
    guess = int(input("Enter the first number randomly generated"))
    while guess != num1:
        print("Your guess is wrong")
        guess=int(input("Enter the first number randomly generated"))

    #While the second guess is incorrect, keep asking the user to guess again
    guess2=int(input("Enter the second number randomly generated"))
    while guess2 != num2:
        print("Your guess is wrong")
        guess2=int(input("Enter the second number randomly generated"))

    print("You guessed both numbers correctly")

def code_2():
    num = input("Please enter a number")
    num = int(num)
    while num > 0:
        print(num)
        num=num-1

def code_3():
    for i in range(1,11):
        print(i)

def code_4():
    item1 = "dress"
    item2 = "shirt"
    item3 = "blouse"
    clothes = [item1, item2, item3]
    for item in clothes:
        print("I like to wear a " + item)

def code_5():
    foods = ["pizza", "tacos","sushi"]
    for food in foods:
        print(food)
    print("just "+foods[2])

def code_6():
    word = "banana"
    for i in word:
        print(i)

def code_7():
    for i in range(10,31):
        print(i)
    
    colors = ["red", "blue", "green","yellow","purple","orange","white"]
    for i in colors:
        print(i)
    
    word = str(input("Enter a word: "))
    x=0
    for i in word:
        x+=1
        print(x,".",i)

def code_8():
    L = [10, -2, 1, 6, 2]
    print(L[1:3])
    print(L[:3])
    print(L[1:])
    print(L[0:4:2])
    print(L[:])
    print(L[::-1])

def code_9():
    pass

if __name__ == "__main__":
    code_8()