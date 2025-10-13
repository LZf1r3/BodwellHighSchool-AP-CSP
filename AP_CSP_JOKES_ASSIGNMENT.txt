while True:
    joke = int(input("Enter a number from 1 to 3 to hear a joke: "))
    if joke == 1:
        print("Why did the student eat his homework?")
        input("Press Enter to see the answer")
        print("Because the teacher told him it was a piece of cake!")
        break
    elif joke == 2:
        print("Why was the math book sad?")
        input("Press Enter to see the answer")
        print("Because it had too many problems.")
        break
    elif joke == 3:
        print("Why don't scientists trust atoms?")
        input("Press Enter to see the answer")
        print("Because they make up everything!")
    else:
        print("Please enter a valid number between 1 and 3.")
        break