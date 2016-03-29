class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, root):
		head = result = ListNode('dummy')

		while root:
			if root.next and root.val == root.next.val:
				duplicate = root.val
				while root and root.val == duplicate:
					root = root.next
			else:
				head.next = root
				head = head.next
				root = root.next
		head.next = None
		return result.next
"""
Remove Duplicates from Sorted List IIBookmark
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""