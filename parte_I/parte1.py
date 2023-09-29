import cv2
import numpy as np
import matplotlib.pyplot as plt

############### Redimensionamento ############### 
def redimencionar_imagem(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    imagem_redimensionada = cv2.resize(imagem, (1024, 1024))
    cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
    cv2.imwrite('imagem_redimensionada.jpg', imagem_redimensionada)
    cv2.imshow('Imagem Original', imagem)
    cv2.waitKey(0)
    
############### Conversor para HSV ############### 
def conversor_hsv(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    cv2.imwrite('imagem_hsv.jpg', imagem_hsv)
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem HSV', imagem_hsv)
    cv2.waitKey(0)

conversor_hsv("parte_I\lena.png")

############### Histograma Colorido ###############
def histograma_colorido(caminho_imagem):
    canal_azul, canal_verde, canal_vermelho = cv2.split(caminho_imagem)
    plt.hist(canal_azul.ravel(), bins=256, color='blue', alpha=0.5)
    plt.hist(canal_verde.ravel(), bins=256, color='green', alpha=0.5)
    plt.hist(canal_vermelho.ravel(), bins=256, color='red', alpha=0.5)
    plt.xlabel('Intensidade de cor')
    plt.ylabel('Número de pixels')
    plt.legend(['Canal Azul', 'Canal Verde', 'Canal Vermelho'])
    plt.title('Histograma Colorido')
    plt.show()

############### Histograma Escala de Cinza ###############
def histograma_escala_cinza(caminho_imagem):
    imagem_cinza = cv2.cvtColor(caminho_imagem, cv2.COLOR_BGR2GRAY)
    plt.hist(imagem_cinza.ravel(), bins=256, color='gray', alpha=0.5)
    plt.xlabel('Intensidade de cinza')
    plt.ylabel('Número de pixels')
    plt.title('Histograma em Escala de Cinza')
    plt.show()

############### Equalização ###############
def equalizacao(caminho_imagem):
    imagem_colorida = cv2.imread(caminho_imagem)
    canal_azul, canal_verde, canal_vermelho = cv2.split(imagem_colorida)
    canal_azul_equalizado = cv2.equalizeHist(canal_azul)
    canal_verde_equalizado = cv2.equalizeHist(canal_verde)
    canal_vermelho_equalizado = cv2.equalizeHist(canal_vermelho)
    imagem_equalizada = cv2.merge((canal_azul_equalizado, canal_verde_equalizado, canal_vermelho_equalizado))
    cv2.imshow('Imagem Original', imagem_colorida)
    cv2.imshow('Imagem Equalizada', imagem_equalizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
############### Canais de Cores Separadamente ###############
def canaisDeCoresSeparadamente(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    canal_h = imagem_hsv[:, :, 0]
    canal_s = imagem_hsv[:, :, 1]
    canal_v = imagem_hsv[:, :, 2]
    zeros = np.zeros_like(canal_h)
    canal_h_bgr = cv2.merge([canal_h, zeros, zeros])
    canal_s_bgr = cv2.merge([zeros, canal_s, zeros])
    canal_v_bgr = cv2.merge([zeros, zeros, canal_v])
    cv2.imshow('Canal H', canal_h_bgr)
    cv2.imshow('Canal S', canal_s_bgr)
    cv2.imshow('Canal V', canal_v_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()