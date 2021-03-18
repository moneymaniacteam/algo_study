#include <iostream>
#include <cstring>
using namespace std;
/*
int square[8][8] = { {1, 1, 0, 0, 0, 0, 1, 1},
	{1, 1, 0 ,0 ,0 ,0, 1 ,1},
	{0, 0, 0, 0, 1, 1, 0, 0},
	{0, 0, 0, 0, 1, 1, 0, 0},
	{1, 0, 0, 0, 1, 1, 1, 1},
	{0, 1, 0, 0, 1, 1, 1, 1},
	{0, 0, 1, 1, 1, 1, 1, 1},
	{0, 0, 1, 1, 1, 1, 1, 1},
};

int square[2][2] = { {1, 0},
	{0, 1}
};
*/
int square[128][128];
int w_count = 0, b_count = 0;
void div(int, int, int);

int main() {
	
	int size;
	cin >> size;
	memset(square, 0, sizeof(square));

	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cin >> square[i][j];
		}
	}

	div(0, 0, size);

	cout << w_count << '\n';
	cout << b_count;
}

void div(int row, int col, int len) {
	int temp_b_count = 0, temp_w_count = 0;
	for (int i = row; i < row+ len; i++) {
		for (int j = col; j < col+len; j++) {
			if (square[i][j]) temp_b_count++;
			else temp_w_count++;
		}
	}

	if (temp_b_count == len*len) b_count++;
	else if (temp_w_count == len * len) w_count++;
	else {
		div(row, col, len / 2);  // left top
		div(row, col + len / 2, len / 2); // right top
		div(row + len / 2, col, len / 2); // left bottom
		div(row + len / 2, col + len / 2, len / 2); // right bottom
	}
	
	return;
}