class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        word_len = 0
        k = 0
        while i < len(s):
            # break when a hash is encountered
            if s[k] == '#':
                word_len = int(s[i:k])
                ans.append(s[k + 1: k + word_len + 1])
                i = k + word_len + 1
                k = i
            k += 1
        return ans


