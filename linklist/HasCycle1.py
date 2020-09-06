# 给定一个链表，判断链表中是否有环。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# set 判断
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        node = head
        while node and node.next:
            if node in s:
                return True
            s.add(node)
            node = node.next
        return False

# 快慢指针
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False