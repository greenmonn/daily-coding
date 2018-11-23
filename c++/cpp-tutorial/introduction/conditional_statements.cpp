#include "../stdc++.h"

using namespace std;

int main() {
    int number;
    cin >> number;
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

    if (number > 9) {
        cout << "number is greater than 9" << endl;
        return 0;
    }

    cout << numberStrings[number - 1] << endl;

    return 0;
}
