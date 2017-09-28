import os
from PIL import Image
# image extension *.png,*.jpg

#sample1
# makes an image with width 100 and heigh 120
source = ['/home/rakes/Desktop']
target_dir = '/home/rakes/Desktop/GenextImage'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

img = Image.open('/home/rakes/Desktop/pp.jpg')

new_width  = 100
new_height = 120


img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('/home/rakes/Desktop/GenextImage/100*120 .jpg')

# for signature 140*60
img = Image.open('/home/rakes/Desktop/ss.jpg')

new_width  = 140
new_height = 60


img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('/home/rakes/Desktop/GenextImage/140*60 .jpg')



#sample2 of 480 * 320 of image
img = Image.open('/home/rakes/Desktop/pp.jpg')

new_width  = 480
new_height = 240


img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('/home/rakes/Desktop/GenextImage/480*240 .jpg')

# for signature 640*320
img = Image.open('/home/rakes/Desktop/ss.jpg')

new_width  = 640
new_height = 320


img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('/home/rakes/Desktop/GenextImage/640*320 .jpg')



#sample3 of 130*170 of image
img = Image.open('/home/rakes/Desktop/pp.jpg')

new_width  = 130
new_height = 170


img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('/home/rakes/Desktop/GenextImage/130*170 .jpg')

# for signature 210*85
img = Image.open('/home/rakes/Desktop/ss.jpg')

new_width  = 210
new_height = 85


img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('/home/rakes/Desktop/GenextImage/210*85 .jpg')
