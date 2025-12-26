from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_beginning(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Optional[Node], data: int) -> None:
        if prev_node is None:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int) -> None:
        cur = self.head

        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return

        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur is None:
            return

        # unlink the node
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Optional[Node]:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data, "-->", end=" ")
            current = current.next
        print('None')

    def reverse(self) -> None:
        """
        Reverses the singly linked list in-place by changing links between nodes
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def _get_middle(self, head: Optional[Node]) -> Optional[Node]:
        """
        Helper method to find the middle element of the linked list
        """
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        mid_index = (count - 1) // 2

        current = head
        for _ in range(mid_index):
            current = current.next

        return current

    def _merge(self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        """
        Recursive helper function to merge two nodes
        """
        dummy = Node(0)
        tail = dummy

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        elif b:
            tail.next = b

        return dummy.next

    def merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sorts the linked list using the Merge Sort algorithm.
        Returns the head of the sorted list.
        """
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next

        # split the list and sort each sublist
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # merge the sorted sublists
        sorted_list = self._merge(left, right)

        return sorted_list

    def merge_sorted_lists(self, list1: 'LinkedList', list2: 'LinkedList') -> 'LinkedList':
        """
        Merges two separate sorted LinkedList objects
        """
        merged_head = self._merge(list1.head, list2.head)

        # new LinkedList wrapper for the result
        result_list = LinkedList()
        result_list.head = merged_head

        return result_list


if __name__ == '__main__':
    first_list = LinkedList()
    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)

    print("Original Linked List:")
    first_list.print_list()

    # test reverse
    first_list.reverse()
    print("Linked List after Reverse:")
    first_list.print_list()

    # test merge sort
    # assign the new head returned by merge_sort back to self.head
    first_list.head = first_list.merge_sort(first_list.head)
    print("Linked List after Merge Sort:")
    first_list.print_list()

    # test merging two sorted lists
    second_list = LinkedList()
    second_list.insert_at_end(2)
    second_list.insert_at_end(12)
    second_list.insert_at_end(22)

    print("-"*50)

    print("Second Sorted List:")
    second_list.print_list()

    merged_list = LinkedList()
    merged_list = merged_list.merge_sorted_lists(first_list, second_list)
    print("Merged Sorted Lists:")
    merged_list.print_list()
