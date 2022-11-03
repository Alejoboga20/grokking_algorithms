const testArray = [20, 23, 33, 4, 5, 1, 3, 1, 3, 0, -1];

const findSmallest = <T>(array: T[]): number => {
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

const sortArray = <T>(array: T[]): T[] => {
	const sortedArray: T[] = [];
	const length = array.length;

	for (let index = 0; index < length; index++) {
		const smallestIndex = findSmallest(array);
		const smallestElement = array.splice(smallestIndex, 1)[0];
		sortedArray.push(smallestElement);
	}

	return sortedArray;
};

console.log(sortArray(testArray));
