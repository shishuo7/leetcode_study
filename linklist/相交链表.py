# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# set 判断
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is headB:
            return headA
        nodeA = headA
        nodeB = headB
        s = set()
        while nodeA:
            s.add(nodeA)
            nodeA = nodeA.next
        while nodeB:
            if nodeB in s:
                return nodeB
            nodeB = nodeB.next
        return None


# 双指针解法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while(nodeA !=nodeB):
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA