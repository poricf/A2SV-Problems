class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        res = ""
        index = bisect_left(values, [timestamp + 1]) - 1
        if index >= 0:
            res = values[index][1]
        return res