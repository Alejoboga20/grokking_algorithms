const testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const recursiveArraySum = (array: number[] = []): number => {
	if (array.length === 0) return 0;

	return array[0] + recursiveArraySum(array.slice(1));
};

console.log(recursiveArraySum(testArray));
console.log(recursiveArraySum([1]));
console.log(recursiveArraySum());
