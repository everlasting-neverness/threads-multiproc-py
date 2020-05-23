import time
from concurrent import futures

start = time.perf_counter()

def do_smth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'

with futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # results = [executor.submit(do_smth, sec) for sec in secs]
    results = executor.map(do_smth, secs)

    # for f in futures.as_completed(results):
    #     print(f.result())

    for result in results:
        print(result)
    

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')