class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        
        ans  = -1

        l = 0
        r = len(self.store[key]) - 1

        while l <= r:
            m = (l+r)//2
            m_value, m_timestamp = self.store[key][m]

            if m_timestamp <= timestamp:
                ans = max(ans, m)
                l=m+1
            else:
                r=m-1
        return "" if ans == -1 else self.store[key][ans][0]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)