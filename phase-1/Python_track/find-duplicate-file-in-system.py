class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        values = defaultdict(list)
        for path in paths:
            root_path, *files = path.split()
            for _file in files:
                file_name, content = _file.split("(")
                values[content[:-1]].append(f"{root_path}/{file_name}")
        
        return [value for value in values.values() if len(value) > 1]