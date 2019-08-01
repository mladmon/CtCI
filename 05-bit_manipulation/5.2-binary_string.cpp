#include <iostream>
#include <bitset>

using namespace std;

void printBinary(double num) {
	bitset<32> binNum;
	int i = 31;
	while (num != 0 && i >= 0) {
		num *= 2;
		if (num >= 1) {
			binNum[i] = 1;
			num -= 1;
		} else {
			binNum[i] = 0;
		}
		--i;
	}

	if (num != 0) {
		cout << "ERROR" << endl;
	} else {
		cout << "0." << binNum << endl;
	}
}

int main () {
	printBinary(0.72);
	printBinary(0.59375);
	printBinary(0.45);
	printBinary(0.625);

	return 0;
}
