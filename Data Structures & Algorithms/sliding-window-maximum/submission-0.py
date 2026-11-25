from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []

        for i in range(len(nums)):

            # Remove indices outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add current index
            q.append(i)

            # Window is formed
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


# Test input
nums = [1, 2, 1, 0, 4, 2, 6]
k = 3

# Create object
sol = Solution()

# Run function
output = sol.maxSlidingWindow(nums, k)

# Print result
print("Input:", nums)
print("Window Size:", k)
print("Output:", output)