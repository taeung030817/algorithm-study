def quick_sort(arr):
    """피벗 기준으로 작은/큰 값을 나눠가며 정렬. 평균 O(n log n), 최악 O(n^2). in-place에 가까움."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print(quick_sort(numbers))
