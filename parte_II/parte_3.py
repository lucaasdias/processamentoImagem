import cv2
import matplotlib.pyplot as plt
import numpy as np


def preencher_buraco_preto(caminho_imagem):
    imagem_colorida = cv2.imread(caminho_imagem,cv2.IMREAD_COLOR)
    imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)
    kn = np.ones((14,14),np.uint8)
    remocao_dos_objetos_pretos = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE,kn)
    fig,ax = plt.subplots(ncols=2,figsize=(15,5))
    ax[0].imshow(imagem_colorida)
    ax[0].set_title('Imagem Colorida')
    ax[1].imshow(remocao_dos_objetos_pretos)
    ax[1].set_title('Remoção dos Objetos Pretos')
    plt.show()


def remocao_objetos_pretos(caminho_imagem):
    imagem_colorida = cv2.imread(caminho_imagem,cv2.IMREAD_COLOR)

    imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)

    kn = np.ones((14,14),np.uint8)
    remocao_dos_objetos_pretos = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE,kn)

    fig,ax = plt.subplots(ncols=2,figsize=(15,5))
    ax[0].imshow(imagem_colorida)
    ax[0].set_title('Imagem Colorida')
    ax[1].imshow(remocao_dos_objetos_pretos)
    ax[1].set_title('Remoção dos Objetos Pretos')

    plt.show()
    
def realce_de_borda(caminho_imagem):

    imagem = cv2.imread(caminho_imagem)
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bordas = cv2.Canny(imagem_gray, 100, 200)  
    cv2.imshow('Bordas Realçadas', bordas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    
    
    
    