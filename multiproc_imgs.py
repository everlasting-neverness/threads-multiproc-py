import time
import os
from concurrent import futures
from PIL import Image, ImageFilter

img_path = 'img'
processed_path = 'processed'

img_names = [
    '1.jpg',
    '2.jpg',
    '3.jpg'
]

start = time.perf_counter()

size = (1200, 1200)

def process_img(img_name):
    img_name_with_path = os.path.join(img_path, img_name)
    img = Image.open(img_name_with_path)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(os.path.join(processed_path, img_name))
    print(f'{img_name} was processed')

def run():
    with futures.ProcessPoolExecutor() as executor:
        executor.map(process_img, img_names)
        
run()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')