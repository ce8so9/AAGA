#!/usr/bin/env python3

import argparse
import random
from timer import Timer

def gen_array(size):
   return [random.randint(-2**31, 2**31) for i in range(size)]

def max_subarray_sum_naive(arr):
    N = len(arr)
    max_sum = 0
    for i in range(0, N):
        curr_sum = 0
        for j in range(i, N):
            curr_sum += arr[j]

            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum

def max_subarray_sum_opt(array, low, high):

    # No element in the array
     if low > high:
         return 0
     # One element in the array
     if low == high:
         return array[low]#max(0, array[low])

     # Middle element of the array */
     middle = (low + high) // 2

     # find maximum sum crossing to left */
     leftMax = sum_count = 0
     for i in range(middle, low, -1):
        sum_count += array[i];
        if sum_count > leftMax:
            leftMax = sum_count;

     # find maximum sum_count crossing to right */
     rightMax = sum_count = 0;
     for i in range(middle+1, high+1, 1):
        sum_count += array[i];
        if sum_count > rightMax:
            rightMax = sum_count;

     # Return the maximum of leftMax, rightMax and their sum */
     return max(leftMax + rightMax, max(max_subarray_sum_opt(array, low, middle), max_subarray_sum_opt(array, middle+1, high)));

def main():
    parser = argparse.ArgumentParser(description='maximum subarray sum performance')
    parser.add_argument("N", help="test array max size", type=int)

    args = parser.parse_args()
    res = 0

    opt_times = []
    naive_times = []

    naive_res = 0
    opt_res = 0

    for i in range(1, args.N, 1000):
        test = gen_array(i)

        with Timer() as t:
            naive_res = max_subarray_sum_naive(test)
        naive_times.append(t.secs)

        with Timer() as t:
            opt_res = max_subarray_sum_opt(test, 0, len(test) - 1)
        opt_times.append(t.secs)
        print(naive_res)
        print(opt_res)

        assert(naive_res == opt_res)

    import matplotlib.pyplot as plt

    plt.plot(range(1, args.N, 1000), naive_times, label="Naive max subarray sum")
    plt.plot(range(1, args.N, 1000), opt_times, label="Optimized max subarray sum")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.xlabel('array size')
    plt.ylabel('time (in secs)')
    plt.show()

if __name__ == "__main__":
    main()
