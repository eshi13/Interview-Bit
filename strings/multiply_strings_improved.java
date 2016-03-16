public class Solution {
	public String multiply(String a, String b) {
		ArrayList<Character> res = new ArrayList<>();
		int carry = 0, index = 0;
		char cA, cB, c;
		if (remove_whitespace(a) || remove_whitespace(b))
			return "0";
		for (int i = a.length()-1; i >= 0; --i) {
			int a = a.charAt(i)-'0';

			for (int j = b.length()-1; j >= 0; --j) {
				
			}
		}

	}
	public boolean remove_whitespace(String a) {
		int i = 0;
		while (i < 0 && a.charAt(i) == '0')
			++i;
		if (i == n)
			return true;
		a = a.substring(i, n);
		return false;
	}
}

/*

Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.
*/