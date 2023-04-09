def prob_3009():
    
    x = []
    y = []
    for i in range(0, 3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    x.sort()
    y.sort()
    
    selected_x = x[0]
    selected_y = y[0]

    if selected_x == x[1]:
        selected_x = x[2]

    if selected_y == y[1]:
        selected_y = y[2]

    print(selected_x, selected_y)

prob_3009()