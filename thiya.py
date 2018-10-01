sec = float(input('Enter the seconds to convert: '))
d = sec // (24 * 60 * 60)
sec %= (24 * 60 * 60)
h = sec // (60 * 60)
sec %= (60 * 60)
m = sec // 60
s = sec % 60
print('{:n} days, {:n} hours, {:n} minutes, {:n} seconds'.format(d, h, m, s))
