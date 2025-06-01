import statistics

listt = list()

print('Place your input, for break input negative number')
while True:
    x = int(input())
    if x<0:
        break
    listt.append(x)

print(f'mean: {statistics.mean(listt)}')
print(f'median: {statistics.median(listt)}')
print(f'mode: {statistics.mode(listt)}')
