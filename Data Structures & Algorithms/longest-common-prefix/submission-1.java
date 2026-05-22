class Solution {
    public String longestCommonPrefix(String[] strs) {

        // If array is empty
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Take the first string as prefix
        String prefix = strs[0];

        // Loop starting from 1 (compare with rest)
        for (int i = 1; i < strs.length; i++) {
            String s = strs[i];

            // Shrink prefix until current string starts with it
            while (!s.startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);

                // If prefix becomes empty, return ""
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        // Return what remains as the prefix
        return prefix;
    }
}
