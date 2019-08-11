'''
This only works correctly if both code and image 
are placed at the same folder, otherwise you'll 
need to get the image path.
'''

from PIL import Image as ig #Python image library

img = ig.open('your_image.format') #Insert path/image name here.
img_w = img.size[0] #Gets image width.
img_h = img.size[1] #Gets image heigth.
'''
The next variables represents the pixels you wanna
count.
I used one to count the pure red pixels (255, 0, 0)
and one to count de maximum amount of pixels.
Feel free to change as your necessity.
'''
count_r = 0 #Pure red pixels.
count_total = 0 #All image pixels.

if (img.mode == "RGB"): #Tests the image color channels.
    for y in range(0, img_h): #Starts to count the image pixels.
      for x in range(0, img_w):
        xy = (x, y)
        rgb = img.getpixel(xy)
        count_total += 1
        if (rgb == (255, 0, 0)):
          count_r +=1
        
else:
    print('Not supported image!')

print(f'Width: {img_w} \nHeigth: {img_h}')
print(f'Maximum amount of pixels: {count_total}\n'
      f'Pure red pixels: {count_r}')

'''
why not maximum amount = width * heigth?
Simple, because (1) this way you can do other operations
as count specific colored pixels, grouping the ones you want
or not, and (2) we work images as if the are 2D matrixes.
'''
