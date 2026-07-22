class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for elem in strs:
            s += f"{len(elem)}#{elem}"
        return s

    def decode(self, s: str) -> List[str]:
        size = len(s)
        print(s)
        i = 0
        result = []
        while (i < size):
            str_len = 0
            # Read the number
            k = i
            while k < size:
                if s[k] == "#":
                    break
                k += 1
            str_len = int(s[i:k])
            final_index = k + str_len
            k += 1
            result.append(s[k:final_index + 1])
            i = final_index + 1
        return result