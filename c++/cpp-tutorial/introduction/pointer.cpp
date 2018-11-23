#include "../stdc++.h"

using namespace std;

void update(int *a, int *b) {
    int plus = *a + *b;

    int absMinus = (*a - *b > 0) ? *a - *b : *b - *a;

    *a = plus;

    *b = absMinus;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
