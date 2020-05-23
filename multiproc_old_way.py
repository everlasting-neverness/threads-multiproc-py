import time
import multiprocessing

start = time.perf_counter()

def do_smth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping')

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_smth, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')