import cv2
import numpy as np

def filtro_prewitt(caminho_imagem):
    imagem = cv2.imread('parte_III\Filtro_Prewitt\coins.png', cv2.IMREAD_GRAYSCALE)
    kernel_x = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]], dtype=np.float32)

    kernel_y = np.array([[-1, -1, -1],
                        [0, 0, 0],
                        [1, 1, 1]], dtype=np.float32)
    prewitt_x = cv2.filter2D(imagem, -1, kernel_x)
    prewitt_y = cv2.filter2D(imagem, -1, kernel_y)
    magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
    magnitude = np.uint8(magnitude)
    cv2.imwrite('coins_prewitt_x.jpg', prewitt_x)
    cv2.imwrite('coins_prewitt_y.jpg', prewitt_y)
    cv2.imwrite('coins_magnitude.jpg', magnitude)
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Prewitt X', prewitt_x)
    cv2.imshow('Prewitt Y', prewitt_y)
    cv2.imshow('Magnitude', magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filtro_prewitt("parte_III\Filtro_Prewitt\coins.png")