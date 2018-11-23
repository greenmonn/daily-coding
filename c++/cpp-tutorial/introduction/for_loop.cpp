#include "../stdc++.h"

using namespace std;

int main() {
    int from, to;

    cin >> from;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cin >> to;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<string> numberStrings = {"one",
                                    "two",
                                    "three",
                                    "four",
                                    "five",
                                    "six",
                                    "seven",
                                    "eight",
                                    "nine",
                                    "ten"};

    for (int i = from; i <= to; i++) {
        if (i <= 9) {
            cout << numberStrings[i - 1] << endl;
        } else if (i % 2 == 0) {
            cout << "even" << endl;
        } else if (i % 2 == 1) {
            cout << "odd" << endl;
        }
    }

    return 0;
}
