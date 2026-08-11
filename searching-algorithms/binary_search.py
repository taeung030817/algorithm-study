def binary_search(arr, target):
    """정렬된 리스트 arr에서 target의 인덱스를 찾는다. 없으면 -1 반환."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    numbers = list(range(1, 1001))  # 1~1000 정렬된 데이터
    target = 777

    result = binary_search(numbers, target)
    print(f"{target}의 인덱스: {result}")
