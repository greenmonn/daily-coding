#include "../stdc++.h"

using namespace std;

vector<int> make_integer_array(int length) {
    vector<int> array;

    for (int j = 0; j < length; j++) {
        int elem;

        cin >> elem;

        array.push_back(elem);
    }

    return array;
}

int main() {

    vector<vector<int>> arrays;
    int arrayCount, queryCount;

    cin >> arrayCount >> queryCount;

    for (int i = 0; i < arrayCount; i++) {
        int length;
        vector<int> array;

        cin >> length;

        array = make_integer_array(length);

        arrays.push_back(array);
    }

    for (int i = 0; i < queryCount; i++) {
        int row, col;

        cin >> row >> col;

        cout << arrays[row][col] << endl;
    }

    return 0;
}