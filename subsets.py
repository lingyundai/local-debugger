from typing import List


class Solution:
    def subsets(self, nums: List[int]):
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res


s = Solution()
print(s.subsets([1, 2, 3]))


# The first call: dfs(0):
# The condition i >= len(nums) is false, so we move forward.
# nums[0] is appended to subset which is now [1].
# A new call is made to dfs(1).

# The second call: dfs(1):
# The condition i >= len(nums) is false, so we move forward.
# nums[1] is appended to subset which is now [1, 2].
# A new call is made to dfs(2).

# The third call: dfs(2):
# The condition i >= len(nums) is false, so we move forward.
# nums[2] is appended to subset which is now [1, 2, 3].
# A new call is made to dfs(3).

# The fourth call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1, 2, 3] is appended to the res list.
# The function returns.

# The third call returns:
# nums[2] is removed from subset which is now [1, 2].
# A new call is made to dfs(3).

# The fifth call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1, 2] is appended to the res list.
# The function returns.

# The second call returns:
# nums[1] is removed from subset which is now [1].
# A new call is made to dfs(2).

# The sixth call: dfs(2):
# The condition i >= len(nums) is false, so we move forward.
# nums[2] is appended to subset which is now [1, 3].
# A new call is made to dfs(3).

# The seventh call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1, 3] is appended to the res list.
# The function returns.

# The sixth call returns:
# nums[2] is removed from subset which is now [1].
# A new call is made to dfs(3).

# The eighth call: dfs(3):
# The condition i >= len(nums) is true, so the current subset [1] is appended to the res list.

# Let's consider the example of the dfs function in the given code. 
# When the function is first called with dfs(0), a new instance of the 
# function is added to the call stack. This instance starts executing and 
# calls dfs(1), which in turn calls dfs(2), and so on.

# When the innermost call to dfs(3) returns, it pops off the call stack, 
# and the control returns to the previous instance of the function, which 
# was waiting for the call to return. The previous instance then continues 
# executing from where it left off, which is the next line of code after the 
# recursive call that just returned.

# In the example you asked about, after the call to dfs(3) returns, the 
# control is returned to the previous instance of the dfs function, which 
# was dfs(2). The code then continues executing from where it left off in the 
# dfs(2) call, which is the next line of code after the dfs(3) call, which is 
# subset.pop(). This line removes the last element from the subset list, and 
# then the code continues with the next line, which is the next recursive call to dfs(3).