import personal_data.resources as personal_res
import sys
import os
from PIL import Image

file_root = os.path.join(personal_res.root, "234_346")


image_1 = Image.open(os.path.join(file_root, "frequency/rel1.png"))
image_2 = Image.open(os.path.join(file_root, "frequency/abs0.png"))

image_list = [image_1, image_2, image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1, image_1]

print(image_1.size)
print(image_1.size[0])

width = image_1.size[0]
height = image_1.size[1]

new_im = Image.new('RGB', (width*5, height*6))




