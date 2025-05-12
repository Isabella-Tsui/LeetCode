class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1Ptr = 0;
        int tempPtr = 0;
        int nums2Ptr = 0;
        int[] temp = new int[m + n];

        // There can be nothing in nums2, but nums1 must have something in it
        // So don't do anything
        if (nums2.length == 0) {
            return;
        }

        // There is something in both arrays
        while (nums1Ptr < m && nums2Ptr < n) {
            if (nums2[nums2Ptr] >= nums1[nums1Ptr]) {
                temp[tempPtr] = nums1[nums1Ptr];
                nums1Ptr++;
            } else {
                temp[tempPtr] = nums2[nums2Ptr];
                nums2Ptr++;
            }
            tempPtr++;
        }

        // Went through all of nums1 but did not reach the end of the nums2
        while (nums2Ptr < n) {
            temp[tempPtr] = nums2[nums2Ptr];
            nums2Ptr++;
            tempPtr++;
        }

        // Went through all of nums2 but did not reach the end of the nums1
        while (nums1Ptr < m) {
            temp[tempPtr] = nums1[nums1Ptr];
            nums1Ptr++;
            tempPtr++;
        }

        // Fill nums1 with the merged array
        for (nums1Ptr = 0; nums1Ptr < nums1.length; nums1Ptr++) {
            nums1[nums1Ptr] = temp[nums1Ptr];
        }
    }
}