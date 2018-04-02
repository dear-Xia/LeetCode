#Definition for singly-linked list.
class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None :
            return None
        elif l1==None :
            return l2
        elif l2==None :
            return  l1
        else :
            return None
if __name__ == "__main__":
    print Solution().mergeTwoLists([1,2,3,4],[])