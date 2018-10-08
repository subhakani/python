def f(string, s, c=0):
    if c < n:
        print(string * s)
        f(string, s, c=c + 1)

f('abc', 3)
