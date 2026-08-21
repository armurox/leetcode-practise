class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += f"{len(st)}#{st}"
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        decoding = False
        size = len(s)
        i = 0
        while (i < size):
            k = i
            while k < size:
                if s[k] == "#":
                    break
                k += 1
            str_len = int(s[i:k])
            final_index = k + str_len
            k += 1
            ans.append(s[k:final_index + 1])
            i = final_index + 1
        return ans


