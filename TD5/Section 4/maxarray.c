#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include "../c_timer/timer.h"

int *ALEA;

void randomize(int *T, int n, int LOW, int HIGH) {
    int i;
    for(i=0;i<n;i++){
        T[i] = rand() % (HIGH - LOW + 1) + LOW;
    }
}

void init(int NBR) {
    ALEA = (int*)calloc(NBR,sizeof(int));
    randomize(ALEA, NBR, -2000, 2000);
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

// A utility funtion to find maximum of two integers
int max2(int a, int b) { return (a > b)? a : b; }
 
// A utility funtion to find maximum of three integers
int max3(int a, int b, int c) { return max2(max2(a, b), c); }
 
// Find the maximum possible sum in arr[] auch that arr[m] is part of it
int
maxCrossingSum(int arr[], int l, int m, int h)
{
    // Include elements on left of mid.
    int sum = 0;
    int left_sum = INT_MIN;
    for (int i = m; i >= l; i--)
    {
        sum = sum + arr[i];
        if (sum > left_sum)
          left_sum = sum;
    }
 
    // Include elements on right of mid
    sum = 0;
    int right_sum = INT_MIN;
    for (int i = m+1; i <= h; i++)
    {
        sum = sum + arr[i];
        if (sum > right_sum)
          right_sum = sum;
    }
 
    // Return sum of elements on left and right of mid
    return left_sum + right_sum;
}

int
maxSubArraySum(int arr[], int l, int h)
{
   // Base Case: Only one element
   if (l == h)
     return arr[l];
 
   // Find middle point
   int m = (l + h)/2;
 
   /* Return maximum of following three possible cases
      a) Maximum subarray sum in left half
      b) Maximum subarray sum in right half
      c) Maximum subarray sum such that the subarray crosses the midpoint */
   return max3(maxSubArraySum(arr, l, m),
              maxSubArraySum(arr, m+1, h),
              maxCrossingSum(arr, l, m, h));
}

void
test(int count){
    srand(time(NULL));
    int i = -1;
    char buffer[50];

    FILE *pFile = NULL;
    pFile = fopen("maxarrdata.txt", "w");

    int naive_res = -1;
    int opt_res = -1;
    srand(time(NULL));
    for (i = 1; i < count; i = i + 1000) {
        init(i);
        init_timer;

        first_step_timer;
        naive_res = naive_max_array_sum(ALEA, i);
        second_step_timer;
        snprintf(buffer, sizeof(buffer), "%d %lf ", i, tim1);
        //printf("%d\n", naive_res);

        first_step_timer;
        opt_res = maxSubArraySum(ALEA, 0, i-1);
        second_step_timer;
        snprintf(buffer+strlen(buffer), sizeof(buffer), "%lf\n", tim1);
        //printf("%d\n", opt_res);

        buffer[strlen(buffer)] = '\0';
        fwrite(buffer, sizeof(char), strlen(buffer), pFile);

        free(ALEA);
        ALEA = NULL;
        assert(naive_res == opt_res);
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
