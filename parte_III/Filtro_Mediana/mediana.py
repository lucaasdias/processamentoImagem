import cv2

def filtro_mediana(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    imagem_suavizada = cv2.medianBlur(imagem, 5)
    cv2.imwrite('lena_ruido_filtro_mediana.jpg', imagem_suavizada)
    cv2.imshow('Lena Filtro Mediana', imagem_suavizada)
    cv2.imshow('Imagem Original', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filtro_mediana("parte_III\Filtro_Mediana\lena_ruido.jpeg")
