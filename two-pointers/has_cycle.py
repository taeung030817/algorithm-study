class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """fast & slow 포인터로 연결 리스트에 사이클이 있는지 판별한다. O(n)."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    # 3 -> 2 -> 0 -> -4 -> (다시 2로 연결, 사이클 발생)
    n4 = ListNode(-4)
    n3 = ListNode(0, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(3, n2)
    n4.next = n2

    print(has_cycle(n1))  # True
