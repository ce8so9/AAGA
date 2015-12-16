public static int FindMaxSumSubArray(int[] array, int low, int high){
 
     /* No element in the array */
     if (low > high)  
        return 0;
     /* One element in the array */
     if (low == high) 
        return max(0, array[low]);
        
     /* Middle element of the array */   
     int middle = (low + high) / 2;
    
     /* find maximum sum crossing to left */
     leftMax = sum = 0;
     for (i = middle; i ≥ low; i--) {
        sum += array[i];
        if (sum > leftMax)
            leftMax = sum;
     }
    
     /* find maximum sum crossing to right */
     rightMax = sum = 0;
     for (i = middle+1; i ≤ high; i++) {
        sum += array[i];
        if (sum > rightMax)
            rightMax = sum;
     }
     
     /* Return the maximum of leftMax, rightMax and their sum */
     return Math.max(leftMax + rightMax, 
     Math.max(FindMaxSumSubArray(low, middle), FindMaxSumSubArray(middle+1, high)));
 }