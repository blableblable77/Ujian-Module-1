def find_short(string):
    y=(string.split(' '))
    a=0
    for i in range(len(y)):
        print((len(y[a+i])),end=' ')
find_short('Many people get up early in the morning')