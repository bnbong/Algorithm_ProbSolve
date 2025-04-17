s = "python"
print(s[:2] + '-' + s[-2:])
print(f'{s[:2]}-{s[-2:]}')

print(s[:2] + '-' + s[-1:-3:-1])

nums = [100, 2, 3, 4, 5]
print(nums)
print(nums + [0, 10, 20])

bts = ['V', 'J-Hope', 'RM', 'Jungkook', 'Jin', 'Jimin', 'Suga']
print('V' in bts)
print('Suga' not in bts)

print(list(s))

heros = ['spiderman', 'blackpanter', 'hulk', 'ironman']
print(heros)

heros.remove('hulk')
print(heros)
print(heros.pop(1))

heros.extend(['superman'])
print(heros)

heros.clear()
print(heros)

c = ['1', 'b', 'h', 'n', 'o', 'oo', 't', 'z']
print(c)
c.sort(reverse=True)
print(c)

a = [5, 4, 3, 2, 1]
b = a
print(id(a), id(b))
a.sort()
print('a:', a)
print('b:', b)

scores = [10, 20, 30, 40, 50]
# 1
values = list(scores)
print(id(scores), id(values))
values[2] = 99
print(scores)
print(values)
# 2
values = scores.copy()
print(id(scores), id(values))
values[2] = 99
print(scores)
print(values)
#3
values = scores[:]
print(id(scores), id(values))
values[2] = 99
print(scores)
print(values)

import copy  # type: ignore

a = [0, [100, 200, 300]]
b = copy.copy(a)
b[0] = 1000
b[1].append(400)
print(f'a: {a}, b: {b}')  # 1차원만 카피

a = [0, [100, 200, 300]]
b = copy.deepcopy(a)
b[0] = 1000
b[1].append(400)
print(f'a: {a}, b: {b}')  # deep copy 2-dim list
