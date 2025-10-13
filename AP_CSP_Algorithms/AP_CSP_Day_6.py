def code_1():
    squares = []
    for i in range(5):
        squares.append(i **2)
    print(squares)

def code_2():
    nums=[1,3,7,6,6,6]
    x=0
    for i in nums:
        x+=i
    print(x)

def code_3():
    nums=[1,3,7,6,6,6]
    x=0
    for i in nums:
        x+=i
    x = x/len(nums)
    print(x)
    

def code_4():
    nums=[1,3,7,6,6,6,-6]
    max_num=nums[0]
    for i in nums:
        if i>max_num:
            max_num=i
    print(max_num)

def code_5():
    nums=[1,3,7,6,6,6.-6]
    x=0
    for i in nums:
        if i%2==0:
            x+=i
    print(x)
    
if __name__ == "__main__":
    code_4()