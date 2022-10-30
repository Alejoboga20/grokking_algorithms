const binarySearch = <T>(list: T[], item: T): number | null => {
	let low = 0;
	let high = list.length - 1;

	while (low <= high) {
		let mid = Math.floor((low + high) / 2);
		let guess = list[mid];

		if (item === guess) return mid;
		if (item < guess) {
			high = mid - 1;
		} else {
			low = mid + 1;
		}
	}

	return null;
};

const orderedList = [0, 3, 4, 5, 6, 7, 8, 8, 11, 12, 13, 15, 16];
console.log(binarySearch(orderedList, 8));
