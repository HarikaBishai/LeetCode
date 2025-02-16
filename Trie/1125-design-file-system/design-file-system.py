class FileSystem:

    def __init__(self):
        self.file_system = {}
        self.value_map = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.value_map:
            return False
        path = path.split("/")[1:]
        
        if not path:
            return False
        
        dir = self.file_system
        last = path[-1]
        for curr in path[:-1]:
            if curr not in dir:
                return False
            dir = dir[curr]
        dir[last] = {}
        self.value_map["/"+ "/".join(path)] = value
        return True



    def get(self, path: str) -> int:
        
        return self.value_map[path] if path in self.value_map else -1
            

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)