/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
	public ListNode reverseBetween(ListNode a, int m, int n) {
		int m1 = m;
		int n1 = n;
		ListNode p1 = a, p2 = a;
		ListNode node_to_insert;

		int i = 1;
		while (i < m-1) {		 // p1 before m
			p1 = p1.next;
			++i;
		}
		i = 1;
		while (i < n-1) {			// p2 before n
			p2 = p2.next;
			++i;
		}
		node_to_insert = p2.next;
		
		p2.next = p2.next.next;
		node_to_insert.next = null;
		
		node_to_insert.next = p1.next;
		p1.next = node_to_insert;

		p1 = p1.next;
		node_to_insert = p2.next;
		p2.next = p2.next.next;
		node_to_insert = null;
		node_to_insert.next = p1.next;
		p1.next = node_to_insert;
	}
}

/*
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. 
*/