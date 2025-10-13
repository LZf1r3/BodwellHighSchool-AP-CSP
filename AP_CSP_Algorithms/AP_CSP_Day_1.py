#This function prints out Hello World and a message about the day using newline comands
def main():
    print("Hello World!")
    print("It has been such a lovely day \ntoday \nbecause school was \nclosed and I saw \nmy friends")

#This function prints out the steps to make a tea
def tea():
    print("This is how you make a tea:")
    print(" 1. Boil water\n 2. Put tea in cup\n 3. Pour water in cup\n 4. Let it soak\n 5. Add milk and sugar (optional)")

#This function asks for the user's name and greets them
def name():
    print("hello World!")
    name = input("What is your name? ")
    print("Hello",name)

def fix():
    name = input("Please enter your name:")
    print("Hi",name)

    food = input("Do you like chocolate cake? ").lower()

    if food == "yes":
        print("Oh goody, so do I")  
    elif food == "no":
        print("that's a shame because i've got some to share")
    else:
        print("please enter a correct answer")

def yes():
    box2= input("please enter your fiend's age:")
    print("your firend is", box2, "years old")
    print("the combined age is:")
    box1 = 16
    print(int(box1)+int(box2))

#Calls the main function to run the program
if __name__ == "__main__":
    yes()
