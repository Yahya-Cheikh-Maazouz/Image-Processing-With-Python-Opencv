import cv2
import numpy as np
from matplotlib import pyplot

# 1 ER FILTRAGE MOYEN

#IMPLEMENTATION DE FILTER MEDIAN

# def filter_median(image, filter_size):
#     temp = []
#     indexer = filter_size // 2
#     for i in range(len(image)):
#
#         for j in range(len(image[0])):
#
#             for z in range(filter_size):
#                 if i + z - indexer < 0 or i + z - indexer > len(image) - 1:
#                     for c in range(filter_size):
#                         temp.append(0)
#                 else:
#                     if j + z - indexer < 0 or j + indexer > len(image[0]) - 1:
#                         temp.append(0)
#                     else:
#                         for k in range(filter_size):
#                             temp.append(image[i + z - indexer][j + k - indexer])
#
#             temp.sort()
#             image[i][j] = temp[len(temp) // 2]
#             temp = []
#     return image




img=cv2.imread("image/dog.png",0)




# creer un figure pour affichage des imqges avec leurs histogrammes
rows = 2
columns = 2
fig = pyplot.figure(figsize=(10, 7))
# 1 ere ligne 1 eme colone
fig.add_subplot(rows, columns, 1)
pyplot.title("image originale")
pyplot.imshow(img,cmap="gray")
# 1 ere ligne 2 eme colone
fig.add_subplot(rows, columns,2)
#img2=filter_median(img,3)
pyplot.title("image filtrer avec filtre median")
img2=cv2.medianBlur(img, 3)
pyplot.imshow(img2,cmap="gray")

# 2 ere ligne 1 eme colone
fig.add_subplot(rows, columns,3)
pyplot.title("image filtrer avec filtre Gaussian")
img3=cv2.GaussianBlur(img, (5, 5), 0.5)
pyplot.imshow(img3,cmap="gray")


pyplot.show()











