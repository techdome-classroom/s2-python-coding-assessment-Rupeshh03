class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the result variable
        total = 0
        
        # Loop through the string `s`
        for i in range(len(s)):
            # If this numeral is smaller than the next one, subtract its value
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            # Otherwise, add its value to the total
            else:
                total += roman_values[s[i]]
        
        # Return the final result
        return tota
