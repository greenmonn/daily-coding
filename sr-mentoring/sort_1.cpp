#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

void print(std::vector<int> v) {
    for (auto it = v.begin(); it != v.end(); ++it)
        std::cout << *it << ' ';
 
    std::cout << '\n';
}

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

vector<int> mergesort(vector<int> seq) {
    if (seq.size() == 1) {
        return seq;
    }

    // divide
    vector<int> left(seq.begin(), seq.begin() + seq.size() / 2);
    vector<int> right(seq.begin() + seq.size() / 2, seq.end());

    left = mergesort(left);
    right = mergesort(right);

    // combine
    vector<int>::iterator l_iter = left.begin();
    vector<int>::iterator r_iter = right.begin();
    vector<int> new_seq;
    
    for (int i=0; i<seq.size(); i++) {
        if (l_iter == left.end()) {
            new_seq.push_back(*r_iter);
            r_iter++;
        } else if (r_iter == right.end()) {
            new_seq.push_back(*l_iter);
            l_iter++;
        } else if (*l_iter > *r_iter) {
            new_seq.push_back(*r_iter);
            r_iter++;
        } else {
            new_seq.push_back(*l_iter);
            l_iter++;
        }
    }
    return new_seq;
}

int main(void) {
    int N;
    vector<int> seq;

    cin >> N;

    for (int i=0; i<N; i++) {
        int num;
        cin >> num;
        seq.push_back(num);
    }

    // merge sort

    vector<int> sorted_seq = mergesort(seq);
    for (int i=0; i<sorted_seq.size(); i++) {
        cout << sorted_seq[i] << endl;
    }

    return 0;
}