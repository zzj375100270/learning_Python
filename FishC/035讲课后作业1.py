#035讲课后作业1
times = [1,3,3.5,6.5,9.5,10,10.8]
names = ['A','B','C','D','E','F','G']
time = []
first_time = 0
for i in range(len(times)):
    time.append(times[i]-first_time)
    first_time = times[i]
zipped = list(zip(names,time))
min_time = min(time)
max_time = max(time)
max_name = [name for name, t in zipped if t == max_time]
min_name = [name for name, t in zipped if t == min_time]
print(f'最快的是{min_name},用时{min_time}秒')
print(f'最慢的是{max_name},用时{max_time}秒')