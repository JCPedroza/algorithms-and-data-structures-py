from typing import Optional as Option
from . import list_node

Node = list_node.ListNode


def add_linklists(anode: Option[Node], bnode: Option[Node]) -> Option[Node]:
    """Add two linked lists that represent digits in a number.
    Uses simple recursion.
    Complexity: time O(n), space O(n).
    :param anode: First node of a linked list.
    :param bnode: First node of a linked list.
    :return: Sum of the two linked lists as a linked list.
    """

    def loop(xnode: Option[Node], ynode: Option[Node], carry=0) -> Option[Node]:
        if xnode or ynode or carry:
            xval = xnode.val if xnode else 0
            yval = ynode.val if ynode else 0
            xnxt = xnode.nxt if xnode else None
            ynxt = ynode.nxt if ynode else None

            total = xval + yval + carry
            return Node(total % 10, loop(xnxt, ynxt, total // 10))

        return None

    return loop(anode, bnode)


solution = add_linklists
name = "simple recursion"
