def insert():
    lst = [1, 2, 3, 4, 5]
    lst.insert(2, 99)
    print(lst)

def pop():
    lst = [1, 2, 3, 4, 5]
    lst.pop(2)
    print(lst)

def split():
    s = "Hello, world"
    words= s.split()
    print(words)

def fun_split():
    fruits = "apple mango banana grape"
    fruits_1st = fruits.split()
    print(fruits_1st) 

    greeting = "hi,I am Mike,I just graduate."
    greet_1st = greeting.split(",")
    print(greet_1st)

    nums="4 24 12"
    nums_1st = nums.split()
    print(nums_1st)

def test():
    L = [3, "hi", -4, 6]
    L.append(2)
    L.insert(1, "hello")
    a = L.pop(3)
    print(a)
    L.pop()
    print(L)

def lab_1():
    l1st = [3,41,62,87,101,88]
    x=0
    for i in  l1st:
        x+=i
    print(x)
    x=0
    for i in range(len(l1st)):
        if l1st[i]%2!=0:
            x+=l1st[i]
    print(x)
    x=0
    for i in l1st[1::2]:
        x+=i
    print(x)

def lab_2():
    num_string= input("Enter a series of numbers, separated by spaces: ")
    num_list = float(num_string.split())
    for i in range(len(num_list)):
        if int(num_list[i])%2==0:
            num_list[i]= 3.1415927
    print(num_list)
    for i in range(len(num_list)):
        max=float(num_list[0])
        if float(num_list[i])>float(max):
            max=num_list[i]
    print(num_list)
    print(max)

def lab_3():
    num_string= input("Enter a series of numbers, separated by spaces: ")
    num_list = num_string.split()
    for i in range(len(num_list)):
        num_list[i]= int(num_list[i])
    
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            num_list[i]= 3.1415927
    max_num=num_list[0]
    for i in range(len(num_list)):
        if num_list[i]>max_num:
            max_num=num_list[i]
    print(max_num)
    
    

if __name__ == "__main__":
    lab_3()