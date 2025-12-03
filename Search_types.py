lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Target = 3
def linear_search(lists, Target):
    for i in lists: 
        if i == Target:
            return print("Found", Target)
    else:
        return print("Not Found", Target)

def binary_search(lists, Target):
    low = 0
    high = len(lists) - 1
    while low <= high:
        mid = (low + high) // 2
        if lists[mid] == Target:
            return print("Found", Target)
        elif lists[mid] < Target:
            low = mid + 1
        else:
            high = mid - 1
    return print("Not Found", Target)

linear_search(lists, Target)
binary_search(lists, Target)