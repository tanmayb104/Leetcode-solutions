public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        int n = s.Length;
        HashSet<char> set = new HashSet<char>();
        int maxLength = 0, i = 0, j = 0;
        while (i < n && j < n)
        {
            if (!set.Contains(s[j]))
            {
                set.Add(s[j++]);
                maxLength = Math.Max(maxLength, j - i);
            }
            else
            {
                set.Remove(s[i++]);
            }
        }
        return maxLength;
    }
}