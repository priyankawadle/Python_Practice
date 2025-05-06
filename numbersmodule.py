def fib_series(num):
    a,b = 0,1
    sum =0
    series = []
    series.append(a)
    series.append(b)
    for each in range(0,num):
        sum = a+b
        series.append(sum)
        a = b
        b = sum
    return series