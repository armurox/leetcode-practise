class Solution:

    def encode(self, strs: List[str]) -> str:
        overall_string = []
        for s in strs:
            temp_string = ""
            count = 0
            for c in s:
                count += 1
                temp_string += c
            temp_string = f'{count}#' + temp_string
            overall_string.append(temp_string)
        return "".join(overall_string)


    def decode(self, s: str) -> List[str]:
        result = []
        size = len(s)
        if size == 0:
            return result
        i = 0
        while i < size:
            j = i
            while s[i] != '#':
                i += 1
            if i == size:
                break
            size_of_word = int(s[j:i])
            result.append(s[i + 1: i + size_of_word + 1])
            i += (size_of_word + 1)
        return result




