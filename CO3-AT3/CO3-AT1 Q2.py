def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid, iterations
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, iterations


sizes = [10, 100, 1000, 10000, 100000]

print("Size\tIterations")

for n in sizes:
    arr = list(range(1, n + 1))
    key = n

    index, iterations = binary_search(arr, key)

    print(f"{n}\t{iterations}")
