class Solution {
    public boolean hasDuplicate(int[] nums) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true; // Duplicate found
            }
            seen.add(num);
        }

        return false; // No duplicates
    }
}
