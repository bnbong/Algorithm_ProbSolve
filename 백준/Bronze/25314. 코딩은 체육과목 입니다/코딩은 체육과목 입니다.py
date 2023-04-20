N = int(input())

string = "int"
long_str = "long "

iterate = N // 4
string = long_str * iterate + string

print(string)
