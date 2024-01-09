class RandomizedSet:

    def __init__(self):
        self.rset = set()
    def insert(self, val: int) -> bool:
        if not val in self.rset:
            self.rset.add(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.remove(val)
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(list(self.rset))
