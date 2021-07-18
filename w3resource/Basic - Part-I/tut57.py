import timeit
import time


print(timeit.timeit("sum(range(1,1000000))",number=1))

start_time = time.time()
sum(range(1,1000000))
end_time = time.time()
print(end_time-start_time)
