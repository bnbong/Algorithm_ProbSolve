def prob_9610():
    spots = int(input())
    results = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}

    for i in range(spots):
        x, y = map(int, input().split())
        if x == 0 or y == 0:
            results['AXIS'] += 1
        elif x > 0 and y > 0:
            results['Q1'] += 1
        elif x < 0 and y > 0:
            results['Q2'] += 1
        elif x < 0 and y < 0:
            results['Q3'] += 1
        elif x > 0 and y < 0:
            results['Q4'] += 1
    
    print('Q1:', results['Q1'],
        '\nQ2:', results['Q2'],
        '\nQ3:', results['Q3'],
        '\nQ4:', results['Q4'],
        '\nAXIS:', results['AXIS'])

prob_9610()