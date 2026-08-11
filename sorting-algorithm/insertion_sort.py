def insertion_sort(arr):
    """정렬된 구간을 하나씩 늘려가며, 새 값을 알맞은 자리에 밀어 넣는다. O(n^2)."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print(insertion_sort(numbers))
