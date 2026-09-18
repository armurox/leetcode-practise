class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Find latest key with timestamp value before hand
        if values := self.storage.get(key):
            # Binary search values
            left = 0
            right = len(values) - 1
            res = ''
            while left <= right:
                middle = (left + right) // 2
                if values[middle][1] > timestamp:
                    right = middle - 1
                else:
                    res = values[middle][0]
                    left = middle + 1
            return res
        else:
            return ""
        
