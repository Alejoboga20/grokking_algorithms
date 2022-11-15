const test_array = [2, 2, 3413, 32, 423131, 4124, 4, 4124, 4, 0, 12, 23, 415789765, 554];

export const quicksort = <T>(array: T[]): T[] => {
	if (array.length < 2) return array;

	const pivot = array[0];
	const less = array.slice(1).filter((element) => element <= pivot);
	const greater = array.slice(1).filter((element) => element > pivot);

	return quicksort(less).concat(pivot, quicksort(greater));
};

console.log(quicksort(test_array));
