def simplifyPath(path: str) -> str:
    stack = []
    dirs = path.split('/')
    print(dirs)
    p, n = 0, len(dirs)
    while p < n:
        dir = dirs[p]
        if dir == '' and p > 0:
            p += 1
            continue
        if dir == '..':
            if stack: stack.pop()  # 前一个 / 出栈
            p += 1
            continue
        if dir == '.':
            p += 1
            continue
        if dir == '/':
            p += 1
            continue
        stack.append(dir)
        p += 1
    print('stack', stack)
    if len(stack) == 0:
        return '/'
    if len(stack) == 1:
        return '/' + stack[0]
    if stack[0] != '':
        return '/' + '/'.join(stack)

    return '/'.join(stack)


def simplifyPath2(path: str) -> str:
    stack = []
    dirs = path.split('/')
    for dir in dirs:
        if dir == '..':
            if stack: stack.pop()
        elif dir and dir != '.':
            stack.append(dir)
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    # path = '/home/'
    # path = '/home//foo/'
    # path = '/home/user/Documents/../Pictures'
    # path = '/../'
    # path = '/.../a/../b/c/../d/./'
    # path = '/a/../../b/../c//.//'
    # path = '/home/../../..'
    # path = '/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///'
    path = '/'
    ans = simplifyPath(path)
    print(ans)
