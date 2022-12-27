def time_converter(seconds):
    hour, second = divmod(seconds, 3600)
    minute, sec = divmod(second, 60)

    return hour, minute, sec

def prob_1408():
    from datetime import datetime

    now = datetime.strptime(input(), '%H:%M:%S')
    then = datetime.strptime(input(), '%H:%M:%S')

    result = (then - now)
    seconds = result.seconds
    hour, minute, sec = time_converter(seconds)

    print('{:02}:{:02}:{:02}'.format(int(hour), int(minute), int(sec)))

prob_1408()