class PartitionResult {
	int leftSize, middleSize;
	public PartitionResult(int left, int middle) {
		this.leftSize = left;
		this.middleSize = middle;
	}
	int[] smallestK(int[] array, int k) {
		if (k <= 0 || k > array.length)	throw new IllegalArgumentException();
		int threshold = rank(array,k-1);
		int[] smallest = new int[k];
	}
}