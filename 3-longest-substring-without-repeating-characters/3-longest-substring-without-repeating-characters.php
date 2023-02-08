<?php

    class Solution {

    /**
     * @param String $s
     * @return Integer
     */
   function lengthOfLongestSubstring($s) {
    $n = strlen($s);
    $set = array();
    $maxLength = 0;
    $i = 0;
    $j = 0;
    while ($i < $n && $j < $n) {
        if (!in_array($s[$j], $set)) {
            $set[] = $s[$j++];
            $maxLength = max($maxLength, $j - $i);
        } else {
            unset($set[array_search($s[$i++], $set)]);
        }
    }
    return $maxLength;
}

}

?>