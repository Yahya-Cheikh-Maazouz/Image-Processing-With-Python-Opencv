import cv2
from matplotlib import pyplot






# PARTIE 1 : CALCUL D'HISTOGRAMMES :
#---------------------------------------------------------------------#
# image1 = np.zeros((4,4), dtype=np.float16)
# image1[0][0]=127/255
# image1[0][1]=127/255
# image1[0][2]=0
# image1[0][3]=1
# image1[1][0]=127/255
# image1[1][1]=0
# image1[1][2]=0
# image1[1][3]=1
# image1[2][0]=127/255
# image1[2][1]=0
# image1[2][2]=0
# image1[2][3]=1
# image1[3][0]=127/255
# image1[3][1]=127/255
# image1[3][2]=0
# image1[3][3]=1
# print(image1)
#pyplot.imshow(image1,cmap="gray")
#pyplot.show()
# pyplot.hist(image1.ravel(),256)
# pyplot.show()


#QUESTION 3 ET 4:
#------------#

# img2=cv2.imread("image/cafe.png")
# img3=cv2.imread("image/coeur.jpeg")
#
# rows = 2
# columns = 2
#
# # creer un figure
# fig = pyplot.figure(figsize=(10, 7))
#
# # Adds a subplot at the 1st position
# fig.add_subplot(rows, columns, 1)
# # showing image
# pyplot.imshow(img2)
#
# # Adds a subplot at the 2nd position
# fig.add_subplot(rows, columns, 2)
# # showing image
# pyplot.hist(img2.ravel(),256)
#
#
# # Adds a subplot at the 3  position
# fig.add_subplot(rows, columns, 3)
# # showing image
# pyplot.imshow(img3)
#
#
# # Adds a subplot at the 1st position
# fig.add_subplot(rows, columns, 4)
# # showing image
# pyplot.hist(img3.ravel(),256)
#
#
# pyplot.show()
# print("debug correct")
# #cv2.waitKey(0)
# cv2.destroyAllWindows()




# PARTIE 2 :NEGATIF D'UNE IMAGE
#---------------------------------------------------------------------#
#
# img=cv2.imread("image/ISABE_LUMI.BMP",0)
#
# #CETTE FONCTION PERMET DE PARCOURIR UNE IMAGE PIXEL
# #PAR PIXEL ET D'INVERSER LA COULEUR
# def inverserCouleur(img):
#     ligne, cols = img.shape
#     for i in range(ligne):
#         for j in range(cols):
#             img[i, j]=255-img[i, j]
#
#
# # creer un figure pour affichage des imqges avec leurs histogrammes
# rows = 2
# columns = 2
# fig = pyplot.figure(figsize=(10, 7))
# # 1 ere ligne 1 eme colone
# fig.add_subplot(rows, columns, 1)
# pyplot.imshow(img,cmap="gray")
# # 1 ere ligne 2 eme colone
# fig.add_subplot(rows, columns,2)
# pyplot.hist(img.ravel(),255)
#
# # 2 eme ligne 1 eme colone
# img2=img
# fig.add_subplot(rows, columns,3)
# inverserCouleur(img2)
# pyplot.imshow(img2,cmap="gray")
#
# # 2 eme ligne 1 eme colone
# fig.add_subplot(rows, columns,4)
# pyplot.hist(img2.ravel(),255)
# pyplot.show()













#PARTIE 3 : ETIREMENT D'HISTOGRAMME :
#---------------------------------------------------------------------#

img=cv2.imread("image/IMG.JPG",0)
img2=img
img3=img

print(img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
pyplot.hist(hist)
pyplot.xlabel("intensite")
pyplot.show()
