#include <stdio.h>

// Create a length 624 array to store the state of the generator
int MT[624];
int ind = 0;

// Initialize the generator from a seed (not the single possible way to initialize the generator !)
void initialize_generator(int seed) {
    ind = 0;
    MT[0] = seed;

    int i;
    for (i = 1; i < 623; i++) {
        MT[i] = (0x6c078965 * (MT[i-1] ^ (MT[i-1] >> 30)) + i) & 0x00000000FFFFFFFF;
    }
}

// Generate an array of 624 untempered numbers
void generate_numbers() {
    int i;
    for (i = 0; i < 623; i++) {
        // bit 31 (32nd bit) of MT[i]
        int y = (MT[i] & 0x80000000) + (MT[(i+1) % 624] % 0x7FFFFFFF);

        // bits 0-30 (first 31 bits) of MT[...]
            MT[i] = MT[(i + 397) % 624] ^ (y >> 1);
            if ((y % 2) != 0) { // y is odd
                MT[i] = MT[i] ^ 0x9908b0df;
            }
    }
}

// Extract a tempered pseudorandom number based on the ind-th value,
// calling generate_numbers() every 624 numbers
int extract_number() {
    if (ind == 0) {
        generate_numbers();
    }

    int y = MT[ind];
    y = y ^ (y >> 11);
    y = y ^ (y << 7) & 0x9d2c5680;
    y = y ^ (y << 15) & 0xefc60000;
    y = y ^ (y >> 18);
    ind = (ind + 1) % 624;
    return y;
}


int main(int argc, const char *argv[])
{
    initialize_generator(234);
    printf("%d\n", extract_number());

    return 0;
}
