import random

# Binary Search Function
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            print(f"Searching for {target}: index = {mid}, steps = {steps}")
            return mid, steps
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Searching for {target}: Not Found!, steps = {steps}")
    return -1, steps

# Function to generate a random list of unique integers
def random_list(n):
    return random.sample(range(1, 10000), n)

#defining lists
L_sorted = sorted(random_list(100))


#Test cases:
binary_search(L_sorted, L_sorted[0]) # Target at the beginning
binary_search(L_sorted, L_sorted[len(L_sorted)//2]) # Target in the middle
binary_search(L_sorted, L_sorted[-1]) # Target at the end
binary_search(L_sorted, 10001) # Target not in the list
