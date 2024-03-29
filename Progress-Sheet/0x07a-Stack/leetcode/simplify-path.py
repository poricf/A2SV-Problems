class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        input      =   /..//abc//./def/a/../
        simplified =   /abc/def
        '''
        stack = []
        Npath = path.split('/')
        print(Npath)
        for c in Npath:
            if c == "..":
                if stack: stack.pop()
            elif c == '.' or  c == '':
                continue
            else:
                stack.append(c)
        
        anspath = "/" + "/".join(stack)
        return anspath
