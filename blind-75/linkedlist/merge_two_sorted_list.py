from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to help with merging
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        # Append the remaining elements
        tail.next = list1 or list2

        return dummy.next


# Helper function to convert a list to a linked list
def create_linked_list(elements):
    dummy = ListNode()
    tail = dummy
    for element in elements:
        tail.next = ListNode(element)
        tail = tail.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)


if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    merge = Solution()
    result = merge.mergeTwoLists(list1, list2)

    print_linked_list(result)
