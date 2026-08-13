def permutations(nums):
    """가능한 모든 순열(n!개)을 생성한다."""
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue                     # 유효하지 않은 선택은 거부
            used[i] = True                   # choose
            path.append(nums[i])
            backtrack()                       # explore
            path.pop()                        # undo
            used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    print(permutations(["a", "b", "c"]))
