#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <limits.h>
#include "../c_timer/timer.h"

int *ALEA;

void randomize(int *T, int n, int LOW, int HIGH) {
    int i;
    srand(time(NULL));
    for(i=0;i<n;i++){
        T[i] = rand() % (HIGH - LOW + 1) + LOW;
    }
}

void init(int NBR) {
    ALEA = (int*)calloc(NBR,sizeof(int));
    randomize(ALEA, NBR, -2000000000, 2000000000);
}

int
naive_max_array_sum(int *T, int N) {
    int max = INT_MIN;
    for (int i = 0; i < N; i++) {
        int sum = 0;
        for (int j = i; j < N; j++) {
            sum += T[j];

            if (sum > max)
                max = sum;
        }
    }

    return max;
}

int
max(int x, int y) {
    if (x < y)
        return y;
    return x;
}

int
opt_max_array_sum(int *T, int low, int high) {

    if (low > high)
        return 0;

    if (low == high)
        return max(0, T[low]);

    int middle = (low + high) / 2;
    int i = -1;

    /* find maximum sum crossing to left */
    int leftMax, rightMax, sum = 0;
    for (i = middle; i >= low; i--) {
        sum += T[i];
        if (sum > leftMax)
            leftMax = sum;
    }

    /* find maximum sum crossing to right */
    for (i = middle+1; i <= high; i++) {
        sum += T[i];
        if (sum > rightMax)
            rightMax = sum;
    }

    /* Return the maximum of leftMax, rightMax and their sum */
    return max(leftMax + rightMax, max(opt_max_array_sum(T, low, middle), opt_max_array_sum(T, middle+1, high)));
}

void test(int count){
    srand(time(NULL));
    int i = -1;
    char buffer[50];

    FILE *pFile = NULL;
    pFile = fopen("maxarrdata.txt", "w");

    for (i = 0; i < count; i = i+100) {
        init(i);
        init_timer;

        first_step_timer;
        naive_max_array_sum(ALEA, i);
        second_step_timer;
        snprintf(buffer, sizeof(buffer), "%d %lf ", i, tim1);

        first_step_timer;
        opt_max_array_sum(ALEA, 0, i-1);
        second_step_timer;
        snprintf(buffer+strlen(buffer), sizeof(buffer), "%lf\n", tim1);

        buffer[strlen(buffer)] = '\0';
        fwrite(buffer, sizeof(char), strlen(buffer), pFile);
    }

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
