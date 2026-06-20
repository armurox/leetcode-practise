class Solution:
    def isPalindrome(self, s: str) -> bool:
        second_pointer = len(s) - 1
        for i in range(len(s) // 2 + 1):
            if not s[i].isalnum():
                continue
            while not s[second_pointer].isalnum():
                second_pointer -= 1
            if s[i].lower() != s[second_pointer].lower():
                return False
            second_pointer -= 1

        return True