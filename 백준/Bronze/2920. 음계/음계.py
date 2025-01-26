music = list(map(int, input().split()))
sorted = music[:]
reversed = music[:]

sorted.sort()
reversed.sort(reverse=True)


if music == sorted:
    print("ascending")
elif music == reversed:
    print("descending")
else:
    print("mixed")
