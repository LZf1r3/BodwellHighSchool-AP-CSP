import random

# Functions

# Linear Search Function
def linear_search(list, target):
    steps = 0
    for value in list:
        steps += 1
        if value == target:
            return steps
    return steps

# Binary Search Function
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return steps
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return steps


sizes = [1000, 10000, 50000, 200000, 800000]
searches = 8

print("Comparing Linear Search and Binary Search (Average Steps)")
print("---------------------------------------------------------")

for N in sizes:

    # create list 1..N
    numbers = []
    for i in range(1, N + 1):
        numbers.append(i)

    # generate 8 random targets
    targets = []
    for i in range(searches):
        rand_num = random.randint(1, N)
        targets.append(rand_num)

    # run linear search 8 times
    linear_steps = []
    for t in targets:
        steps_taken = linear_search(numbers, t)
        linear_steps.append(steps_taken)

    # run binary search 8 times
    binary_steps = []
    for t in targets:
        steps_taken = binary_search(numbers, t)
        binary_steps.append(steps_taken)

    # compute integer averages
    total_lin = 0
    for s in linear_steps:
        total_lin += s
    avg_linear = total_lin // searches

    total_bin = 0
    for s in binary_steps:
        total_bin += s
    avg_binary = total_bin // searches

    print(f"\nN = {N}")
    print(f" Linear Search Avg Steps: {avg_linear}")
    print(f" Binary Search Avg Steps: {avg_binary}")
