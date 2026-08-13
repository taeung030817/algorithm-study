def subsets(nums):
    """모든 부분집합을 생성한다. 원소마다 choose -> explore -> undo."""
    result = []
    path = []

    def backtrack(start):
        result.append(path.copy())          # 현재까지 담긴 것도 유효한 부분집합
        for i in range(start, len(nums)):
            path.append(nums[i])            # choose
            backtrack(i + 1)                 # explore
            path.pop()                       # undo

    backtrack(0)
    return result


if __name__ == "__main__":
    print(subsets(["a", "b"]))
    # [[], ['a'], ['a', 'b'], ['b']]
