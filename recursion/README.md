# 5. Recursion (재귀)

## 개념

재귀는 같은 문제의 더 작은 버전을 자기 자신에게 호출해서 해결하는 방식이다.

## 성립하기 위한 3가지 요소

1. **Base case**: 프로세스를 멈추는 조건
2. **Smaller sub-problem**: 원래보다 작아진 하위 문제
3. **Guaranteed progress**: 매 호출마다 base case 방향으로 확실히 나아가는 것

이 세 가지 중 하나라도 없으면 함수는 멈추지 않고 계속 자기 자신을 호출한다.

**예시**: `factorial(5)`

```
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1                ← base case
```

여기서 각 호출마다 문제가 작아지고(n → n-1), 결국 n=1이라는 base case에 도달한다.

## 예시로 이해하기: 트리 순회 (Tree Traversal)

1. 현재 노드가 없다면 (`None`) → 함수 종료 (base case)
2. 노드가 있다면 → 왼쪽 자식 탐색 → 현재 노드 처리 → 오른쪽 자식 탐색

노드가 몇 개든 이 규칙은 똑같이 적용된다. 자식 노드는 나무의 뿌리처럼 계속 더 작은 트리로 갈라진다.

## 호출이 진행되는 동안 컴퓨터는 무엇을 하고 있을까: Call Stack

더 큰 호출은 작은 호출이 끝날 때까지 기다린다. 아직 끝나지 않은(대기 중인) 호출들은 **call stack**에 차곡차곡 쌓인다.

이게 base case가 중요한 이유다. Base case는 더 깊이 들어가는 걸 멈추고, 쌓여있던 호출들을 거꾸로 돌아나가게(return) 만드는 시작점이다. 이 스택에 쌓이는 비용이 재귀가 치르는 대가다.

- **Balanced tree**: 낮은 depth로도 많은 노드를 담을 수 있어 스택 부담이 적다.
- **Skewed tree** (한쪽으로 치우쳐 리스트처럼 늘어진 트리): 노드 수는 같아도 depth가 훨씬 깊어진다. 완료되지 않은 호출이 계속 쌓이면서 스택이 부족해질 수 있다 (스택 오버플로우).

## Merge Sort, Quick Sort도 재귀다

둘 다 큰 문제를 작은 문제로 계속 축소해나가는 방식으로 동작한다.

**주의**: 재귀를 쓴다고 알고리즘이 저절로 빨라지는 건 아니다. 예를 들어 naive(단순) 피보나치 재귀는 같은 값을 여러 번 다시 계산하기 때문에 불필요한 작업을 반복한다.

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2) ...
│   │   └── fib(1)
│   └── fib(2) ...        ← fib(3) 계산할 때 나온 fib(2)와 중복 계산!
└── fib(3) ...             ← 위에서 이미 계산한 fib(3)을 또 계산!
```

이 중복 계산 문제는 나중에 **Dynamic Programming**에서, "매번 다시 계산하는 대신 한 번 계산한 값을 저장해두는 방법"으로 해결한다.

## Tail Recursion

재귀 호출이 함수의 마지막 동작이고, 그 호출 뒤에 더 처리할 작업이 남아있지 않은 경우를 tail recursion이라고 한다.

이 경우 이론적으로는 새로운 스택 층을 쌓지 않고 같은 스택 공간을 재사용해서 loop처럼 동작시킬 수 있다 (tail call optimization). 다만 이건 일부 언어/런타임에서만 지원되는 최적화이고, Python을 포함한 많은 인기 런타임 환경은 이 최적화를 보장하지 않는다.

## 언제 재귀를 써야 할까

데이터나 문제가 본질적으로 재귀적인 구조일 때 사용한다.

- 트리(Trees)
- 중첩된 폴더 구조 (nested folders)
- 분할정복 문제 (divide and conquer)
- 여러 갈래로 뻗어나가는 탐색 (branching search path)

일직선(straight line)으로 진행되는 문제는 그냥 loop가 낫다. 재귀를 쓰면 불필요하게 깊어질 수 있다.

**핵심**: 재귀는 코드 줄 수를 줄여주기 때문이 아니라, 코드의 구조가 문제의 형태를 그대로 반영하기 때문에 유용하다.

## 다음 주제

지금까지 본 예시들은 정해진 하나의 경로만 따라갔다. 그런데 만약 여러 선택지 중 하나를 골라야 하고, 그 선택이 막다른 길이면 다시 되돌아가서 다른 선택을 시도해야 한다면?

재귀 함수는 추측하고, 틀리면 되돌아가고(backtrack), 이전 결정을 취소하는 데에도 쓸 수 있다 → 다음 주제: **Backtracking**.

## 코드

- [`factorial.py`](./factorial.py) — 가장 기본적인 재귀 (base case, 축소, 진행)
- [`tree_traversal.py`](./tree_traversal.py) — 이진 트리 in-order 순회
- [`fibonacci_naive.py`](./fibonacci_naive.py) — naive 재귀가 왜 느린지 보여주는 예시
