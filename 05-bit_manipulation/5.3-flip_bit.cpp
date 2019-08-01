#include <iostream>

using namespace std;

int flipBit(int num) {
	if (num == -1)
		return sizeof(int)*8;

	int curSeq = 0, nextSeq = 0, longestSeq = 0;
	int runningCount = 0;
	for (int i=0; i < sizeof(int)*8; ++i) {
		if (num & 1) {
			++runningCount;
		} else {
			nextSeq = runningCount;
			if (nextSeq + curSeq + 1 > longestSeq) {
				longestSeq = nextSeq + curSeq + 1;
			}
			curSeq = (num & 2) ? nextSeq : 0;
			runningCount = 0;
		}
		num >>= 1;
	}

	// could've ended on a 1, check last sequence
	if (runningCount + curSeq + 1 > longestSeq)
		longestSeq = runningCount + curSeq + 1;

	return longestSeq;
}

int main() {
	cout << "flipBit(1775): " << flipBit(1775) << endl;
	cout << "flipBit(-1): " << flipBit(-1) << endl;
	cout << "flipBit(0b0111111011011101111): " 
				<< flipBit(0b0111111011011101111) << endl;
	cout << "flipBit(0b111111011011101111): " 
				<< flipBit(0b111111011011101111) << endl;
	cout << "flipBit(0b1111110011011101111): " 
				<< flipBit(0b1111110011011101111) << endl;
	cout << "flipBit(0b10100001): " << flipBit(0b10100001) << endl;

	return 0;
}
