import cv2
import numpy as np

def filtro_sobel(caminho_imagem):
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

    sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)

    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Sobel X', sobel_x)
    cv2.imwrite('coins_sobel_x.jpg', sobel_x)
    cv2.imshow('Sobel Y', sobel_y)
    cv2.imwrite('coins_sobel_y.jpg', sobel_y)
    cv2.imshow('Magnitude', magnitude)
    cv2.imwrite('magnitude.jpg', magnitude)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

filtro_sobel("parte_III\Filtro_Sobel\coins.png")