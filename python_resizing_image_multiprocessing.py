import os
import glob
import multiprocessing
import concurrent.futures
import time

from PIL import Image
from PIL import ImageFilter

image_files  = glob.glob('C:/Users/nntan/Pictures/Saved Pictures/*.png')

def resize_image(image_file):
    image = Image.open(image_file)
    image = image.filter(ImageFilter.GaussianBlur(10))
    basename = os.path.basename(image_file)
    image.save(f"C:/Users/nntan/Pictures/resize/{basename}")

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(resize_image, image_files)

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# process ko chia se vung nho voi nhau, doc lap nhau
# thread chia se vung nho cho nhau
# xu ly nhanh thi start thread
# su dung thread de bi race condition
