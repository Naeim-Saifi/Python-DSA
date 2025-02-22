def merge(arr1, arr2):
    l3 = []
    p1 = 0
    p2 = 0
    n1=len(arr1)
    n2=len(arr2)
    while p1 < n1 or p2 < n2:
        v1 = arr1[p1] if p1 < len(arr1) else float('inf')
        v2 = arr2[p2] if p2 < len(arr2) else float('inf')
        if v1 < v2:
            l3.append(v1)
            p1 += 1
        else:
            l3.append(v2)
            p2 += 1
    return l3

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = merge(nums1, nums2)
    n = len(merged)
    if n % 2 == 1:
        # Median is the middle element for odd length
        med = float(merged[n // 2])
    else:
        # Median is the average of the two middle elements for even length
        #index started from 0 that's -1 is taken
        med = (merged[n // 2 - 1] + merged[n // 2]) / 2.0
    return med

nums1 = [1,3,5]
nums2 = [2,4,6]
print(findMedianSortedArrays(nums1,nums2))