#include <iostream>
#include <cmath>

using namespace std;

int R = 31;
int M = 1234567891;

int compute_hash(int L, string seq) {
    int hash = 0;
    for (int i=0; i<L; i++) {
        int a = seq[i] - 'a' + 1;
        // cout << hash << endl;
        hash += (a * int(pow(R, i))) % M;
    }

    return hash;
}

int main(void) {
    int L;
    string seq;

    cin >> L;
    cin >> seq;

    cout << compute_hash(L, seq) << endl;
    return 0;
}