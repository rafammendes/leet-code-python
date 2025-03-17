from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    global head
    global result
    if not list1 or not list2:
        if list1:
            return list1
        if list2:
            return list2
        return None

    if list1.val <= list2.val:
        head = ListNode(list1.val)
        list1 = list1.next
    else:
        head = ListNode(list2.val)
        list2 = list2.next

    result = head

    while list1 or list2:
        if not list1:
            result.next = ListNode(list2.val)
            result = result.next
            list2 = list2.next
            continue
        if not list2:
            result.next = ListNode(list1.val)
            result = result.next
            list1 = list1.next
            continue

        if list1.val <= list2.val:
            result.next = ListNode(list1.val)
            result = result.next
            list1 = list1.next
        else:
            result.next = ListNode(list2.val)
            result = result.next
            list2 = list2.next

    return head

node5 = ListNode(5)

node1 = ListNode(1)
node2 = ListNode(2)
node4 = ListNode(4)

node1.next = node2
node2.next = node4

result = mergeTwoLists(node5, node1)

while result:
    print(result.val)
    result = result.next
