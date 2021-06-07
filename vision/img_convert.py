# python .\img_convert.py C:\work\img_test_jpg C:\work\img_test\img_test_png 
# 원본 이미지 폴더 / 변경 이미지 폴더
# jpg -> png 변환



import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    print(f'A folder named {output_folder} already exists!')


images = os.listdir(image_folder)

# print(images)

for image in images:
    img = Image.open(f'{image_folder}/{image}')
    cleaned_name = os.path.splitext(image)[0]
    img.save(f'{output_folder}/{cleaned_name}.png', 'png')

print("Done!")

# python .\img_convert.py C:\work\img_test_jpg C:\work\img_test\img_test_png 
# 원본 이미지 폴더 / 변경 이미지 폴더
