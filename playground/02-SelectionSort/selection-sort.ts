const testArray = [20, 23, 33, 4, 5, 1, 3, 1, 3, 0, -1];

const findSmallest = (array: number[]): number => {
	let smallestNumber = array[0];
	let smallestIndex = 0;

	for (let index = 0; index < array.length; index++) {
		if (array[index] < smallestNumber) {
			smallestNumber = array[index];
			smallestIndex = index;
		}
	}

	return smallestIndex;
};

if (findSmallest(testArray) === 10) {
	console.log('Correct');
} else {
	throw new Error('Incorrect');
}
