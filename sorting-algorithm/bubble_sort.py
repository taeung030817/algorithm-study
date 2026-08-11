def bubble_sort(arr):
    """인접한 두 값을 비교해서 순서가 틀리면 교체. O(n^2)."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print(bubble_sort(numbers))
