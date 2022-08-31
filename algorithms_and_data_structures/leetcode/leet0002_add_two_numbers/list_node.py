class ListNode:
    """A node in a linked list."""

    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

    def __eq__(self, other) -> bool:
        anode = self
        bnode = other

        while anode and bnode:
            if anode.val != bnode.val:
                return False
            anode = anode.nxt
            bnode = bnode.nxt

        return anode is None and bnode is None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        current = self
        numstr = ""

        while current:
            numstr = str(current.val) + numstr
            current = current.nxt

        return numstr
