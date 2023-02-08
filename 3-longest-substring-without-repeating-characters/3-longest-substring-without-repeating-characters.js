var lengthOfLongestSubstring = function(s) {
    let n = s.length;
    let set = new Set();
    let maxLength = 0, i = 0, j = 0;
    while (i < n && j < n) {
        if (!set.has(s.charAt(j))) {
            set.add(s.charAt(j++));
            maxLength = Math.max(maxLength, j - i);
        } else {
            set.delete(s.charAt(i++));
        }
    }
    return maxLength;
};