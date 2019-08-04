#include <iostream>
#include <utility>
#include <bitset>

using namespace std;

pair<int, int> nextNumber(int num) {
	int posFirstOne, posLastOne = 0; // vars for next largest
	int posSecondOne; // additional var for next smallest

	// find the position of the first 1
	for (int i=0; i < sizeof(int)*8; ++i) {
		if (num & (1 << i)) {
			posFirstOne = i;
			break;
		}
	}

	// find position of the last 1 in the first sequence of 1s
	for (int i=posFirstOne; i < sizeof(int)*8; ++i) {
		if (!(num & (1 << i))) {
			posLastOne = i - 1;
			break;
		}
	}

	// find next largest number
	int nextLargest = num;
	nextLargest |= (0b1 << posLastOne+1);
	nextLargest &= ~(0b1 << posLastOne);
	if (posFirstOne > 0) {
		for (int i=0; i < posFirstOne; ++i) {
			nextLargest |= (0b1 << posFirstOne-1-i);
			nextLargest &= ~(0b1 << posLastOne-1-i);
		}
	}

	// find next smallest number
	int nextSmallest = num;
	if (posFirstOne > 0) {
		nextSmallest |= (0b1 << posFirstOne-1);
		nextSmallest &= ~(0b1 << posFirstOne);
	} else {
		// find the position of the first 1 in the second sequence of 1s
		posSecondOne = posLastOne;
		for (int i=posLastOne+1; i < sizeof(int)*8; ++i) {
			if (num & (0b1 << i)) {
				posSecondOne = i;
				break;
			}
		}

		nextSmallest |= (0b1 << posSecondOne-1);
		nextSmallest &= ~(0b1 << posSecondOne);
		if (posSecondOne-posLastOne > 2) {
			int numShifts = posSecondOne-posLastOne-2;
			for (int i=0; i < numShifts; ++i) {
				nextSmallest |= (0b1 << (posLastOne++)+1);
				nextSmallest &= ~(0b1 << (posFirstOne++));
			}
		}
	}

	return pair<int, int> {nextSmallest, nextLargest};
}

int main() {
	int num = 178;
	cout << "num: " << num << " " << bitset<8>{num} << endl;
	while (num > 15) {
		num = nextNumber(num).first;
		cout << "next smallest: " << num << " " << bitset<8>{num} << endl;
	}

	num = 31;
	cout << endl << "num: " << num << " " << bitset<8>{num} << endl;
	for (int i=0; i < 7; ++i) {
		num = nextNumber(num).second;
		cout << "next largest:  " << num << " " << bitset<8>{num} << endl;
	}

	return 0;
}
