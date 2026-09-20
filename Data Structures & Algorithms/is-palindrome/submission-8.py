class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_pointer = 0
        size = len(s)
        second_pointer = size - 1
        while (first_pointer <= second_pointer and (first_pointer < size) and second_pointer < size):
            while first_pointer < size and not s[first_pointer].isalnum():
                first_pointer += 1
            while second_pointer >= 0 and not s[second_pointer].isalnum():
                second_pointer -= 1
            if first_pointer < size and second_pointer >= 0 and s[first_pointer].lower() != s[second_pointer].lower():
                return False
            first_pointer += 1
            second_pointer -= 1
        return True