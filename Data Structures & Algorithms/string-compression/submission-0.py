class Solution:
    def compress(self, chars: List[str]) -> int:
        # Start with an empty string
        s = ""

        # loop through chars, counting up consecutive chars
        prev = chars[0]
        curr_count = 0
        for elem in chars:
            if elem == prev:
                curr_count += 1
            else:
                s += f"{prev}{curr_count}" if curr_count != 1 else f"{prev}"
                curr_count = 1
                prev = elem
        s += f"{prev}{curr_count}" if curr_count != 1 else f"{prev}"

        # store it in the input array
        k = len(s)
        for i in range(k):
            chars[i] = s[i]
        return k
