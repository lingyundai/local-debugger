from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            p = l
            pivot = nums[r]

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p < k:
                return quickSelect(p+1, r)
            elif p > k:
                return quickSelect(l, p-1)
            else:
                return nums[p]


        return quickSelect(0, len(nums) - 1)

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
