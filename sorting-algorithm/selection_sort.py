def selection_sort(arr):
    """남은 구간에서 최솟값을 찾아 앞으로 옮긴다. O(n^2), swap 횟수는 적다."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print(selection_sort(numbers))
