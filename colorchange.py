import numpy as np
import cv2
import os


origin_pic = "test.jpg"
save_folder = './generated_pics'
try:
    os.makedirs(save_folder)
except OSError:
    pass

img = cv2.imread(origin_pic)
valid_index = []
for color_type in range(-500, 1000, 1):
    try:
        img_new = cv2.cvtColor(img, color_type)
        cv2.imwrite(os.path.join(save_folder, str(color_type)+'.jpg'), img_new)
        valid_index.append(color_type)
        
    except:
        pass
print ('Valid index in cv2.cvtColor:\n{}'.format(valid_index))

cv2.destroyAllWindows()
