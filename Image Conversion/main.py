import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "image/IMG.JPG"
destPath="image/"
newImage=destPath+"Image copie.JPG"
img=cv2.imread(path,1)

# informations
print( 'classe :', type(img) )
print( 'type :', img.dtype )
print( 'taille :', img.shape )


b, g, r = cv2.split(img)
image = cv2.merge([r, g, b])
plt.imshow(img)
plt.show()



# cv2.imwrite(newImage,img)
#
#
#
# window_name = 'image'
# cv2.imshow(window_name, img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()






