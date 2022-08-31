from . import repo_add_two
from . import list_node

ListNode = list_node.ListNode
solutions = repo_add_two.solutions

n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)

n31 = ListNode(1, ListNode(3))
n123 = ListNode(3, ListNode(2, ListNode(1)))
n437 = ListNode(7, ListNode(3, ListNode(4)))
n765 = ListNode(5, ListNode(6, ListNode(7)))
n888 = ListNode(8, ListNode(8, ListNode(8)))
n919 = ListNode(9, ListNode(1, ListNode(9)))
n1202 = ListNode(2, ListNode(0, ListNode(2, ListNode(1))))


def test_add_two():
    for subject in solutions:
        assert subject.solution(n0, n0) == n0
        assert subject.solution(n1, n0) == n1
        assert subject.solution(n1, n1) == n2
        assert subject.solution(n123, n765) == n888
        assert subject.solution(n437, n765) == n1202
        assert subject.solution(n31, n888) == n919

        assert str(n1202) == "1202"
