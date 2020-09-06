# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# set 判断
class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        node = head
        while node and node.next:
            if node in s:
                return node
            s.add(node)
            node = node.next
        return None


# 快慢指针
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                flag = True
                break
        if flag:
            pass
        else:
            return None


# k -> 走到链表入口节点的步数
# f -> 快指针走的步数
# s -> 慢指针走的步数

# f = 2s
# f = s + nb

# s = nb
# f = 2nb

# k = a + nb