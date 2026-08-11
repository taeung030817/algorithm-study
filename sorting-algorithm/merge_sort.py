def merge_sort(arr):
    """반으로 계속 나누고(divide), 다시 합치면서(merge) 정렬. O(n log n). 보조 리스트 필요."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 5, 6]
    print(merge_sort(numbers))
