class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed_string = ''.join([char.lower() for char in s if char.isalnum()])
        return fixed_string.lower() == fixed_string[::-1].lower()