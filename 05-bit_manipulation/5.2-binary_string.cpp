#include <iostream>
#include <bitset>
#include <string>

using namespace std;

string printBinary(double num) {
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
		return "ERROR";
	}
	return "0." + binNum.to_string();
}

int main () {
	cout << "0.72: " << printBinary(0.72) << endl;
	cout << "0.59375: " << printBinary(0.59375) << endl;
	cout << "0.45: " << printBinary(0.45) << endl;
	cout << "0.625: " << printBinary(0.625) << endl;

	return 0;
}
