#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <string.h>

#include "../c_timer/timer.h"

float *ALEA;

void randomize(float *T, int n) {
    int i;
    srand(time(NULL));
    for(i=0;i<n;i++){
        T[i] = (float)rand()/((float)RAND_MAX);
    }
}

void init(int NBR) {
    ALEA = (float*)calloc(NBR,sizeof(float));
    randomize(ALEA,NBR);
}

void
naive_min_max(float *T, int n, float *out_min, float *out_max) {
    float min, max;
    min = max = T[0];
    int i = -1;
    for (i = 1; i < n; i++) {
        if (T[i] < min)
            min = T[i];
        if (T[i] > max)
            max = T[i];
    }

    *out_min = min;
    *out_max = max;
}

void
min_max_32(float *T, int n, float *out_min, float *out_max) {
    float min, max;
    min = max = T[n-1];
    int i = -1;
    for (i = 0; i < n-1; i += 2){
        if (T[i] < T[i+1]) {
            if (T[i] < min) min = T[i];
            if (T[i+1] > max) max = T[i+1];
        }
        else {
            if (T[i+1] < min) min = T[i+1];
            if (T[i] > max) max = T[i];
        }
    }

    *out_min = min;
    *out_max = max;
}

void
test_naive(int n){
    float min, max;

    init_timer;
    first_step_timer;
    naive_min_max(ALEA, n, &min, &max);
    second_step_timer;
    print_time("naive");
    printf("(%f,%f)\n",min,max);
}

void
test_32(int n){
    float min, max;

    init_timer;
    first_step_timer;
    min_max_32(ALEA, n, &min, &max);
    second_step_timer;
    print_time("3/2");
    printf("(%f,%f)\n",min,max);
}

void test(int n){
    float min, max;
    int i = -1;
    char buffer[50];

    FILE *pFile = NULL;
    pFile = fopen("data.txt", "w");

    for (i = 1; i < n; i += 100) {
        init(i);
        init_timer;

        /////// Optimized minimum and maximum searching ///////
        first_step_timer;
        min_max_32(ALEA, i, &min, &max);
        second_step_timer;
        snprintf(buffer, sizeof(buffer), "%d %lf ", i, tim1);

        /////// Naive minimum and maximum searching ///////
        first_step_timer;
        naive_min_max(ALEA, i, &min, &max);
        second_step_timer;
        snprintf(buffer+strlen(buffer), sizeof(buffer), "%lf\n", tim1);

        buffer[strlen(buffer)] = '\0';
        fwrite(buffer , sizeof(char), strlen(buffer), pFile);
    }

    fclose(pFile);
}

int
main(int argc, const char *argv[])
{
    if (argc != 2) {
        exit(-1);
    }

    int max_size = atoi(argv[1]);
    printf("%d\n", max_size);

    if (max_size < 1) {
        exit(-1);
    }

    test(max_size);

    return 0;
}
