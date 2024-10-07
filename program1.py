class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to hold matching pairs
        matching = {')': '(', '}': '{', ']': '['}
        
        # Stack to hold the opening brackets
        stack = []
        
        # Traverse through each character in the string
        for char in s:
            if char in matching.values():  # If it's an opening bracket
                stack.append(char)
            elif char in matching:  # If it's a closing bracket
                # If the stack is empty or the top doesn't match
                if not stack or stack.pop() != matching[char]:
                    return False
        
        # If the stack is empty, all brackets were properly matched
        return not stack







    



  

