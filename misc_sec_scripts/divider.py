import time

times = []
for z in range(100):
    start = time.time()
    [print(i,'Y') if i and not (i&(i-1)) else print(i,'N') for i in range(1000000)]
    end = time.time()
    times.append(end - start)

total = 0
for val in times:
    total += val

algo_one = total/len(times)
print(str(algo_one) + ' seconds')

times = []
for j in range(100):
    start = time.time()
    for n in range(1000000):
        k = n
        while k%2 == 0 and k!=0:
            k = k/2
        if k==1:
            print(n, 'Y')
        else:
            print(n, 'N')
    end = time.time()
    times.append(end - start)

total = 0
for val in times:
    total += val 

algo_two = total/len(times)
print(str(algo_two) + 'seconds')


print('The linear algorithm is ' + str(algo_two/algo_one) + ' times faster than the original one')
