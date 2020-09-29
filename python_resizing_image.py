import multiprocessing
import concurrent.futures
import time
import os
import glob

from PIL import Image
from PIL import ImageFilter

image_files = glob.glob('C:/Users/nntan/Pictures/Saved Pictures/*.png*')
#print(image_files)

def resize_image(image_file):
    image=Image.open(image_file)
    image=image.filter(ImageFilter.GaussianBlur(10)) #lam mo hinh
    base_name=os.path.basename(image_file)
    image.save(f"C:/Users/nntan/Pictures/resize/{base_name}")

start=time.perf_counter()

for image_file in image_files:
    resize_image(image_file)

finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
