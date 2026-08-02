# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=headA
        l1=0
        while a:
            l1+=1
            a=a.next
        b=headB
        l2=0
        while b:
            l2+=1
            b=b.next
        diff=abs(l2-l1)
        b=headB
        a=headA
        if l2>l1:
            for i in range(0,diff):
                b=b.next
        if l1>l2:
            for i in range(0,diff):
                a=a.next
        while a:
            if a==b:
                return a
            a=a.next
            b=b.next
            


        