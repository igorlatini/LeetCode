# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        carrier = 0
        sum_value = l1.val + l2.val + carrier
        if sum_value >= 10:
            carrier = 1
            sum_value -= 10
        else:
            carrier = 0
        result.val = sum_value
        if self.checkEnd(l1,l2,carrier,result):
            return result
        l1 = l1.next
        l2 = l2.next
        nx = ListNode()
        result.next = nx
        while(True):
            sum_value = l1.val + l2.val + carrier
            if sum_value >= 10:
                carrier = 1
                sum_value -= 10
            else:
                carrier = 0
            nx.val = sum_value
            if self.checkEnd(l1, l2, carrier, nx):
                return result
            l1 = l1.next
            l2 = l2.next
            nx.next = ListNode()
            nx = nx.next
            

    def checkEnd(self, l1, l2, carrier, result):
        if l1.next == None and l2.next == None:
            if carrier == 1:
                result.next = ListNode()
                result = result.next
                result.val = 1
                result.next = None
            return True
        elif l2.next == None:
                result.next = ListNode()
                result = result.next
                self.goThrough(l1.next, carrier, result)
                return True
        elif l1.next == None:
            result.next = ListNode()
            result = result.next
            self.goThrough(l2.next, carrier, result)
            return True
        return False
        
    def goThrough(self, ll, carrier, result):
        while(True):
            result.val = ll.val + carrier
            if result.val >= 10:
                result.val = result.val - 10
                carrier = 1
            else:
                carrier = 0
            if ll.next == None:
                if carrier == 1:
                    result.next = ListNode()
                    result = result.next
                    result.val = 1
                    result.next = None
                return
            else:
                ll = ll.next
                result.next = ListNode()
                result = result.next

#General idea: go through each node, check if the sum will carry. Also check for the end of both linked lists