#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <stdlib.h>

int64_t rand48(int64_t n) {
    return (25214903917L * n + 11L) % ((int64_t) pow(2, 48));
}

int java(int64_t n) {
    int64_t res = (rand48(n) >> 16);
    return (int)res;
}

int main(int argc, const char *argv[])
{
    if (argc != 3) {
        exit(-1);
    }

    int64_t x = atoll(argv[1]);
    printf("%ld\n", x);
    int times = atoi(argv[2]);
    int i;
    for (i = 0; i < times; i++) {
        x = java(x);
        printf("%ld\n", x);
    }

    return 0;
}
