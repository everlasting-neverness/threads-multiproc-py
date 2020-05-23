import time
import threading

start = time.perf_counter()

def do_smth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping')

treads = []

for _ in range(10):
    t = threading.Thread(target=do_smth, args=[1.5])
    t.start()
    treads.append(t)

for thread in treads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')