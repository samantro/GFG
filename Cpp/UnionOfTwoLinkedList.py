class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        s = set()
        while head1:
            s.add(head1.data)
            head1 = head1.next
        while head2:
            s.add(head2.data)
            head2 = head2.next
        res = linkedList()
        p = sorted(s)
        for i in p:
            res.insert(i)
        return res.head
        