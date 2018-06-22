import cv2
import numpy as np


#converte a imagem para a escala de cinza
img = cv2.imread('comLuz2.jpg',0)
#Aplica a tranformada de gauss para reduzir o ruido na imagem
suave = cv2.GaussianBlur(img, (7,7), 0)
#aplica o detector de borda
edges = cv2.Canny(suave, 10, 100)
#edges = cv2.Canny(img, 10, 100)

#salva a imagem com o filtro aplicado
cv2.imwrite('borda_comLuz_suave.png', edges)
