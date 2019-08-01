#include <iostream>
#include <bitset>

using namespace std;

int insertMN(int M, int N, int i, int j) {
	int mask = ~(((1 << (j+1)) - 1) & (-1 << i));
	int result = N & mask;
	result |= (M << i);

	return result;
}

// Let's test it!
int main() {
	int result = insertMN(19, 1024, 2, 6);
	cout << result << ": " << bitset<16>(result) << endl;

	return 0;
}
