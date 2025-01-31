sik = input().split('-')

result = 0

first_sum = sum(map(int, sik[0].split('+')))

result += first_sum

for i in sik[1:]:
    _sum = sum(map(int, i.split('+')))
    result -= _sum

print(result)
