#include <iostream>
#include <cmath>
#include <unordered_map>

using namespace std;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    int M;
    string seq;

    cin >> N;
    cin >> M;

    unordered_map<string, string> hashmap;

    string siteAddress;
    string password;

    for (int i=0; i<N; i++) {
        cin >> siteAddress;
        cin >> password;
        hashmap[siteAddress] = password;
    }

    for (int i=0; i<M; i++) {
        cin >> siteAddress;
        cout << hashmap[siteAddress] << "\n";
    }
    return 0;
}