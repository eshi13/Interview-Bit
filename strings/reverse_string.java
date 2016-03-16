public class Solution {
	public String reverseWords(String a) {
	    a = a.trim();
		String[] tokens = a.split(" +"); // one or more spaces
		int n = tokens.length-1;
		for (int i = 0; i < tokens.length/2; ++i) {
			String temp = tokens[i];
			tokens[i] = tokens[n-i];
			tokens[n-i] = temp;
		}
		StringBuilder sb = new StringBuilder();
		int i = 0;
		while (i < tokens.length-1){
			sb.append(tokens[i]); sb.append(" ");
			++i;
		}
		sb.append(tokens[i]);

		return sb.toString();
	}
}
/*
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".
*/