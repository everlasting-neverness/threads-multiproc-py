import time
import requests
import os
from concurrent import futures

start = time.perf_counter()

img_path = 'img/'

img_urls = [
    'https://images.unsplash.com/photo-1590164411927-606a1319b93e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    'https://images.unsplash.com/photo-1590172692993-6aa0f2d6f798?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    'https://images.unsplash.com/photo-1590172116902-195d25d3f894?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
]

def download_image(url):
    img_bytes = requests.get(url).content
    img_name = url.split('/')[-1]
    img_name = os.path.join(img_path, f'{img_name}.jpg')
    with open(img_name, 'wb') as file:
        file.write(img_bytes)
        print(f'{img_name} was downloaded...')

def run():
    with futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)
        
run()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')