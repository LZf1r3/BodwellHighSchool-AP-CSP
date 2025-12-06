def linear_search(list, target):
    steps = 0
    for index, value in enumerate(list):
        steps += 1
        if value == target:
            print(f"Searching for {target}: index = {index}, steps = {steps}")
            return index, steps
    print(f"Searching for {target}: Not Found! steps = {steps}")
    return -1, steps


#Case A
L = [37,12,59,8,44,21,99,3,56,78]

Case_A = 37
linear_search(L, Case_A)  # Target at start of the list

Case_B = 44
linear_search(L, Case_B)  # Target in the middle of the list

Case_C = 78
linear_search(L, Case_C)  # Target at end of the list

Case_D = 100
linear_search(L, Case_D)  # Target not in the list