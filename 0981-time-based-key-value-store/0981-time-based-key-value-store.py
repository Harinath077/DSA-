class TimeMap:
    """  
    {
    "foo": [
        [1, "bar1"],
        [4, "bar2"]
        ]
    }
    """
    def __init__(self):
        self.mapp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapp:
            self.mapp[key] = []
        self.mapp[key].append( (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mapp:
            return ""
        
        arr = self.mapp[key]
        
        # floor
        low = 0
        high = len(arr)-1
        ans = ""

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)