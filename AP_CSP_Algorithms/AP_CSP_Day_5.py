'''This is to reinforce the powerpoint from yesterday, please use your notes. Help eah other out if you don't understand.



1. List Creation and Types 

Create three lists: 
An empty list 
A list of integers containing the values 2, 3, 5, 7, 11 
A list containing mixed data types (e.g., 1, "two", 3.14, -2) 
Print each list and its length. 
 

2. Indexing and Modifying Lists 

Access and print the first, second, and last elements of your integer list. 
Attempt to access an out-of-bounds index and catch the error with a try/except statement. 
Change the first element to 100 and the third element to -4, then print the updated list. 
 

3. List Slicing 

Use slicing to print: 
The first three elements 
All except the first element 
Every second element in reverse order. 
 

4. List Traversal 

Traverse your integer list twice: 
Using a for-each loop, print each value. 
Using a for-loop with indices, print each value. 
 

5. Modifying a List in a Loop 

Write a loop that sets all even values in a list to 0 and prints the result. 
Explain why this works (or doesn’t) if you use a for-each loop instead of indices
'''




def code_1(lists):
    print("List Creation and Types Task 1:")
    for i in range(len(lists)):
        print(str(lists[i])+" Length: "+ str(len(lists[i])))
        print('\n')






def code_2(list):
    print("\nIndexing and Modifying Lists Task 2:")
    print(list[:2:] + [list[-1]])
    try:
        print(list[10])
    except IndexError:
        print("Index out of bounds")
    list[0]=100
    list[2]=-4
    print(list)



def code_3(lists):
    print("\nList Slicing Task 3:")
    for i in range(len(lists)):
        print(lists[i][:3])
        print(lists[i][1:])
        print(lists[i][::-2])
        print('\n')



def code_4(list):
    print("\nList Traversal Task 4:")
    print("For-each loop:")
    for i in list:
        print(i)
    print("\nFor loop with indices:")
    for j in range(len(list)):
        print(list[j])


list1 = []
list2 = [2,3,5,7,11,12]
list3 = [1,"two",3.14,-2]
lists = [list1,list2,list3]

def code_5(lists):
    print("\nModifying a List in a Loop Task 5:")
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            try:
                if (lists[i][j])%2==0:
                    lists[i][j]=0
            except TypeError:
                pass
        print(lists[i])
    """This works with indices because we are directly picking and changing the values within the list. On the contrary, a for-each loop would be changing a 'variable' and not the actual list."""

code_5(lists)

code_1(lists)
code_2(list2)
code_3(lists)
code_4(list2)
code_5(lists)