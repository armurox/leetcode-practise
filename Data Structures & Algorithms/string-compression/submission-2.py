class Solution:
    def compress(self, chars: List[str]) -> int:
        # loop through chars, counting up consecutive chars
        prev = chars[0]
        curr_count = 0
        k = 0
        for elem in chars:
            if elem == prev:
                curr_count += 1
            else:
                # write in the compressed string at every break point
                # into the input array
                chars[k] = prev
                k += 1
                if curr_count != 1:
                    str_curr_count = str(curr_count)
                    for item in str_curr_count:
                        chars[k] = item
                        k += 1
                curr_count = 1
                prev = elem
        chars[k] = prev
        k += 1
        if curr_count != 1:
            str_curr_count = str(curr_count)
            for elem in str_curr_count:
                chars[k] = elem
                k += 1

        # store it in the input array
        return k
