#include "../stdc++.h"

using namespace std;

int main() {
    int N;
    int *array;

    cin >> N;

    array = new int[N];

    for (int i = 0; i < N; i++) {
        cin >> array[N - 1 - i];
    }

    for (int j = 0; j < N; j++) {
        cout << array[j] << " ";
    }

    return 0;
}
