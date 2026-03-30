class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(nums1) + len(nums2)

        targetLen = total//2
        l = 0
        h = len(A) - 1
        while True:
            aLeftI = (l + h)//2
            bLeftI = targetLen - aLeftI - 2

            aLeft = A[aLeftI] if aLeftI >= 0 else -math.inf
            aRight = A[aLeftI + 1] if (aLeftI + 1) < len(A) else math.inf 

            bLeft = B[bLeftI] if bLeftI >= 0 else -math.inf            
            bRight = B[bLeftI + 1] if (bLeftI + 1) < len(B) else math.inf 

            print(aLeft, aRight, bLeft, bRight)

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight))/2
            
            elif aLeft > bRight:
                h = aLeftI - 1
            elif bLeft > aRight:
                l = aLeftI + 1
            
        

            