import cv2
import numpy as np

def particionamento_binarizacao(caminho_imagem):
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    num_divisoes = 2  
    altura, largura = imagem.shape
    quadrados_binarizados = []
    tamanho_quadrado = min(altura, largura) // num_divisoes
    for y in range(0, altura, tamanho_quadrado):
        for x in range(0, largura, tamanho_quadrado):
            quadrado = imagem[y:y+tamanho_quadrado, x:x+tamanho_quadrado]
            _, quadrado_binarizado = cv2.threshold(quadrado, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            quadrados_binarizados.append(quadrado_binarizado)

    for i, quadrado_binarizado in enumerate(quadrados_binarizados):
        cv2.imshow(f'Quadrado {i}', quadrado_binarizado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

particionamento_binarizacao("parte_III\Particionar_Binarizacao\margaridas.png")