import java.util.HashSet;
import java.util.Set;

public class Technical {
    public static int longestSubstringWithoutRepeatingChars(String s) {
        
        Set<Character> set = new HashSet<>();
        int left = 0;
        int res = 0;
        for(int right = 0; right< s.length(); right++){
            while(set.contains(s.charAt(right))){
                 set.remove(s.charAt(left));
            }
                 set.add(s.charAt(right));
                 left++;
            
            res = Math.max(res, right - left + 1);
            }
            return res;
        }

    public static void main(String[] args) {
        // Test cases for longest substring without repeating characters
        System.out.println(longestSubstringWithoutRepeatingChars("abcabcbb")); // Output: 3
        System.out.println(longestSubstringWithoutRepeatingChars("bbbbb"));    // Output: 1
        System.out.println(longestSubstringWithoutRepeatingChars("pwwkew"));   // Output: 3
        System.out.println(longestSubstringWithoutRepeatingChars(""));         // Output: 0
        System.out.println(longestSubstringWithoutRepeatingChars("au"));       // Output: 2
        System.out.println(longestSubstringWithoutRepeatingChars("dvdf"));     // Output: 3


    }
}
