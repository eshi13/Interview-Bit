/* Binary Search */
public class Solution {
	public double findMedianSortedArrays(final List<Integer> A, final List<Integer> B) {
		int len = A.size() + B.size();
		if (len % 2 == 1)																	// Odd
			return findKth(A, 0, B, 0, len/2+1);
		else
			return (findKth(A, 0, B, 0, len/2) + findKth(A, 0, B, 0, len/2 + 1)) / 2.0;		// Even
	}
	public int findKth(List<Integer> A, int a_start, List<Integer> B, int b_start, int k) {
		if (a_start >= A.size())
			return B.get(b_start + k-1);
		if (b_start >= B.size())
			return A.get(a_start + k-1);
		if (k == 1)
			return Math.min(A.get(a_start), B.get(b_start));

		int a_key = a_start + k/2 - 1 < A.size() ? A.get(a_start + k/2 - 1) : Integer.MAX_VALUE;
		int b_key = b_start + k/2 - 1 < A.size() ? A.get(b_start + k/2 - 1) : Integer.MAX_VALUE;

		if (a_key < b_key)
			return findKth(A, a_start + k/2, B, b_start, k - k/2);
		else 
			return findKth(A, a_start, B, b_start + k/2, k - k/2);

	}
}

/**
 * Odd
 * [1, 2, 3, 4, 5] = len(5)/2 + 1 = 3
 * Even
 * NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 
 * For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 
 */