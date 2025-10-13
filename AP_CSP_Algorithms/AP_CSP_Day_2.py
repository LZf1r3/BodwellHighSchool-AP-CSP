def dice_game():
    import random #importing the random library

    print("Welcome to the dice game")
    name = input("Please enter your name: ")

    num = random.randint(1,6) #generating a random number between 1 and 6

    print("hello", name, "I am going to roll the dice, what do you thik the number will be?")

    guess = int(input("Enter your guess: ")) #asking the user to input their guess and converting it to an integer

    if guess == num:
        print("Excellent", name, "you guessed it correct")
    else:
        print("Your guess was wrong")

def code1():
    num1 = int(input("Please enter a number between 5 to 10:"))
    num2 = int(input("Please enter another number between 5 to 10:"))

    answer = num1 + num2

    if answer > 14:
        print("The sum of the two number is bigger than 14")

    input("Press Enter on the keyboard to exit")

def code2():
    num1 = int(input("Please enter a number between 5 to 10:"))
    num2 = int(input("Please enter another number between 5 to 10:"))

    answer = num1 + num2

    if answer > 14:
        print("The sum of the two number is bigger than 14")
    else:
        print("The sum of the two number is less than or equal to 14")

    input("Press Enter on the keyboard to exit")

def random_num():
    import random

    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    print("I have just rolled 2 dice, the numbers produced are: ", num1, "and", num2)

    answer = str(input("Type 'add' if you wish to add the two numbers or 'sub' if you wish to subtract the two numbers: ")).lower()

    if answer == "add":
        print(num1 + num2)
    elif answer == "sub":
        print(num1 - num2)
    else:
        print("I do not understand your response")
        
def test():
    y= 7==6 or 8>=4
    print(str(y))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
if __name__ == "__main__":
    test()