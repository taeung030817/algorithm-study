def solve_n_queens(n):
    """N-Queens. 같은 열/대각선에 위험이 있으면 즉시 가지치기(pruning)."""
    solutions = []
    cols = set()
    diag1 = set()  # row - col (왼쪽 위 -> 오른쪽 아래 대각선)
    diag2 = set()  # row + col (오른쪽 위 -> 왼쪽 아래 대각선)
    placement = []

    def backtrack(row):
        if row == n:
            solutions.append(placement.copy())
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # 유효하지 않은 선택 -> 가지치기

            cols.add(col)                    # choose
            diag1.add(row - col)
            diag2.add(row + col)
            placement.append(col)

            backtrack(row + 1)                # explore

            cols.remove(col)                  # undo
            diag1.remove(row - col)
            diag2.remove(row + col)
            placement.pop()

    backtrack(0)
    return solutions


if __name__ == "__main__":
    solutions = solve_n_queens(4)
    print(f"4-Queens 해의 개수: {len(solutions)}")
    print("예시 해:", solutions[0])
