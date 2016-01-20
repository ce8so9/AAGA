#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "../c_timer/timer.h"

float
classicalpow(float x, int n) {
    float r = 1;
    while (n > 0) {
        if (n & 1)
            r = r * x;
        n /= 2;
        x = x * x;
    }
    return r;
}

float
unrolledpow(float x, int n) {
    float r = 1;
    float t = 0;

    while (n > 0) {
        t = x * x;
        if (n & 1)
            r = r * x;
        if (n & 2)
            r = r * t;
        n /= 4;
        x = t * t;
    }

    return r;
}

float
guidedpow(float x, int n) {
    float r = 1;
    float t = 0;

    while (n > 0) {
        t = x * x;
        if (n & 3) {
            if (n & 1)
                r = r * x;
            if (n & 2)
                r = r * t;
        }
        n /= 4;
        x = t * t;
    }

    return r;
}

/*we computed the floating-point value*/
/*of x n using each of the algorithms 5.10 7 times, with n chosen uniformly at random in*/
/*{0, . . . , 2 26 − 1}*/
void test(int count){
    srand(time(NULL));
    int i = -1;
    char buffer[50];
    float x = 2;
    int n = -1;

    FILE *pFile = NULL;
    pFile = fopen("expdata.txt", "w");

    init_timer;
    first_step_timer;
    for (i = 0; i < count; i++) {
        // 67108864 = 2**26
        n = (float)rand()/((float)RAND_MAX) * 67108863;
        classicalpow(x, n);
    }
    second_step_timer;
    snprintf(buffer, sizeof(buffer), "%s %lf\n", "Classical", tim1);
    buffer[strlen(buffer)] = '\0';
    fwrite(buffer, sizeof(char), strlen(buffer), pFile);

    first_step_timer;
    for (i = 0; i < count; i++) {
        n = (float)rand()/((float)RAND_MAX) * 67108863;
        unrolledpow(x, n);
    }
    second_step_timer;
    snprintf(buffer, sizeof(buffer), "%s %lf\n", "Unrolled", tim1);
    buffer[strlen(buffer)] = '\0';
    fwrite(buffer, sizeof(char), strlen(buffer), pFile);

    first_step_timer;
    for (i = 0; i < count; i++) {
        n = (float)rand()/((float)RAND_MAX) * 67108863;
        guidedpow(x, n);
    }
    second_step_timer;
    snprintf(buffer, sizeof(buffer), "%s %lf\n", "Guided", tim1);
    buffer[strlen(buffer)] = '\0';
    fwrite(buffer, sizeof(char), strlen(buffer), pFile);

    fclose(pFile);
}

int
main(int argc, const char *argv[]) {

    if (argc != 2) {
        exit(-1);
    }

    int size = atoi(argv[1]);
    printf("%d\n", size);

    if (size < 1) {
        exit(-1);
    }

    test(size);

    return 0;
}
