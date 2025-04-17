import copy


a = [1, 2, 3]
b = a
c = list(a)
c2 = a.copy()
c3 = a[:]

print(a, b, c, c2, c3)

a = [0, [100, 200, 300]]
b = copy.deepcopy(a)
b[0] = 1000
b[1].append(400)

print(f'a = {a}, b = {b}')

t1 = (1,)
t2 = (1)
t3 = 1,
u = t1, 4, 5, 6, 7  # packing
print(u)
print(type(t1), type(t2), type(t3), type(u))

t = (1, 2, [10, 20, 30])
print(t)
t[2][0] = 100
print(t)
t[2].append(40)
print(t)

try:
    t[2] = [0, 0, 0]  # error
except:
    print("error occured")

my_tuple = ('p', 'y', 't', 'h', 'o', 'n')
try:
    del my_tuple[3]  # error
except:
    print("cannot delete tuple's element")

addr = "bnbong@hanyang.ac.kr"
name, domain = addr.split('@')
print(name, domain)

s = {1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 5, 4, 6}
print(s)
n = [1 ,2 ,3, 4, 1, 2, 3]
print(n)
n = list(set(n))
print(n)
myset = {1.23, 2, (1, 2, 3), 'hello'}
print(myset)  # list의 출력 결과를 쓸 때 대괄호 없이 쓰거나 list 내 문자열이 있는 경우 출력 결과를 잘 써야함 (생성하는 형태 있는 그대로 써야함)
string = set('python')
print(string)
print('p' in string)
try:
    test = set([1, [2, 3]])
    print(test)
except:
    print("cannot hash multi list")

word = {'one', 'two', 'three'}
print(word)
print(len(word))
print(max(word))
print(min(word))

t = {'foo', 'bar', 'baz', 'qux'}
print(t)
t.update(['a', 'b'])
print(t)

d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
print(type(d))
d[1] = 'c'
print(d)
del d[3]
print(d)
