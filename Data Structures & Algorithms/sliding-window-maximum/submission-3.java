

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new LinkedList<>();
        int[] res = new int[nums.length - k + 1];
        int index = 0;

        for (int i = 0; i < nums.length; i++) {

            // Remove indices that are outside the current window
            while (!q.isEmpty() && q.peekFirst() <= i - k) {
                q.pollFirst();
            }

            // Remove smaller elements from the back
            while (!q.isEmpty() && nums[q.peekLast()] < nums[i]) {
                q.pollLast();
            }

            // Add current index
            q.offerLast(i);

            // Record maximum when window is formed
            if (i >= k - 1) {
                res[index++] = nums[q.peekFirst()];
            }
        }

        return res;
    }
}