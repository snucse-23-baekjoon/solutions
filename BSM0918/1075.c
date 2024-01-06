/*1075. 나누기
#include <stdio.h>

int main() {
    int N,F;
    scanf("%d", &N);
    scanf("%d", &F);

    N /= 100;
    N *= 100;

    for (int i = 0; i < 100; i++){
        if ((N+i) % F == 0){
            printf("%02d", i);
            return 0;
        }

    }
} */
