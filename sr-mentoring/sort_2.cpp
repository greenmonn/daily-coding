#include <stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);

    int counter[10001] = {0,};

    for (int i=0; i<N; i++) {
        int num;
        scanf("%d", &num);
        counter[num]++;
    }

    for (int i=0; i<10001; i++) {
        int count = counter[i];
        if (count > 0) {
            for (int j=0; j<count; j++) {
                printf("%d\n", i);
            }
        }
    }

    return 0;
}