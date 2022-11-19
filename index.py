import cv2
import glob as gb
import numpy as np

branco = [255, 255, 255]
preto = [0, 0, 0]

def processaImagem(imagem):
    img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 230, 150)
    return img;

arrayImagens = gb.glob('./src/*.jpg')
for arquivoImagem in arrayImagens:
    contador = 0
    imagem = cv2.imread(arquivoImagem)
    imagemProcessada = processaImagem(imagem)
    cv2.floodFill(imagemProcessada, None, (0, 0), branco)

    cv2.imshow('Imagem filtrada', imagemProcessada)
    altura, largura = imagemProcessada.shape
    for i in range(altura):
        for j in range(largura):
            if all(imagemProcessada[i, j] == preto):
                size = cv2.floodFill(imagemProcessada, None, (j, i), branco)
                if(size[0] > 35):
                    contador += 1 

    print('Total na imagem:', contador)
    cv2.waitKey(0)
