#This procedure greets the user by their name input
def greet_user(name):
    print("Hello", name+"! Welcome to Python")
#Task 1
my_name = "Lucas"
greet_user(my_name)
#challenge
greet_user(str(input("Please enter your name: ")))

#This function returns the square of a number
def square_number(num):
    return num * num
#Task 2
var = square_number(5)
print("5 squared is", var)
#challenge
num=int(input("number: "))
print(num," squared is", square_number(num))


#This function returns double the input number
def double_number(num):
    return num * 2

#This procedure shows the double of a number
#  using the double_number function
def show_double(num):
    print("Double of", num, "is", double_number(num))
#Task 3
num_input=int(input("Please enter a number to double: "))
show_double(num_input)
number=8
show_double(number)

#Mini calculator
#This function adds two numbers and returns the result
def add_numbers(num1, num2):
    return num1 + num2
#This function multiplies two numbers and returns the 
# result
def multiply_numbers(num1, num2):
    return num1 * num2
#This procedure shows the sum and product of two numbers using the add_numbers and multiply_numbers functions
def calculator(num1, num2):
    print("The sum is", add_numbers(num1, num2),". The product is", multiply_numbers(num1, num2),".")
#Task 4
calculator(int(input("number1: ")), int(input("number2: ")))

#Number Guessing Helper
#This function checks if the guess is correct
def is_correct_guess(guess, target):
    if guess == target:
        return True
    else:
        return False
#This procedure gives a hint if the guess is too low or too high
def give_hint(guess, target):
    if guess < target:
        print("Too low!")
    else:
        print("Too high!")
#This procedure runs the number guessing game based on the give_hint and is_correct_guess functions
def guessing_game():
    import random
    target = random.randint(1, 20)
    attempts = 0
    while True:
        guess = int(input("Enter your guess (1-20): "))
        attempts += 1
        if is_correct_guess(guess, target):
            print("Congratulations! You've guessed the number in", attempts, "attempts.")
            break
        elif attempts >= 5:
            print("sorry, you've used all your attempts. The number was", target)
            break
        else:
            give_hint(guess, target)
#Task 5
guessing_game()

#Main program








