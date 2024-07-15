import ast
for _ in range(int(input())):
    func, num, arr, flag, reverse = input(), int(input()), ast.literal_eval(input()), 0, False
    for f in func:
        if f == 'R':
            reverse = not reverse
        elif f == 'D':
            if flag := (len(arr) == 0): break
            arr.pop(len(arr)-1 if reverse else 0)
    print("error" if flag else str(arr[::-1] if reverse else arr).replace(" ", ""))
