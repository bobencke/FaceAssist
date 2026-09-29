#Bibliotecas
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from deepface import DeepFace
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import cv2

#Classe Construtora
class FaceAssist:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Assist")
        #Inicializa captura de imagem com o OPENCV
        self.webcam = cv2.VideoCapture(0)
        #Inicializa janela da interface tekinter
        self.criarWidgets()
        self.atualizarFrame()
        #Inicializa variavel está com dúvida como 0
        self.estaComDuvida = False

    #Função inicializa todo o conteúdo da interface tekinter
    def criarWidgets(self):
        self.janela = tk.Frame(self.root)
        self.janela.pack(padx=10, pady=10)

        self.webcamContainer = tk.Canvas(self.janela, width=640, height=480)
        self.webcamContainer.pack()

        self.rotuloEmocao = ttk.Label(self.janela, font=("Arial", 10), text="Emoção: ")
        self.rotuloEmocao.pack(pady=5)

        self.rotuloIdade = ttk.Label(self.janela, font=("Arial", 10), text="Idade: ")
        self.rotuloIdade.pack(pady=5)

        self.rotuloProbabilidadeDuvida = ttk.Label(self.janela, font=("Arial", 10), text="Probabilidade de Dúvida: ")
        self.rotuloProbabilidadeDuvida.pack(pady=5)

        self.botaoDetectar = ttk.Button(self.janela, text="Detectar", command=self.detectarEmocaoEIdade)
        self.botaoDetectar.pack(pady=10)

    #Função lê a webcam e representa a imagem dentro da interface
    def atualizarFrame(self):
        ret, frame = self.webcam.read()
        if ret:
            self.frameAtual = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.frameAtual))
            self.webcamContainer.create_image(0, 0, image=self.photo, anchor = tk.NW)

        self.root.after(10, self.atualizarFrame)
    #Utilizando a biblioteca DeepFace, armazenamos valores retornados nas suas respectivas listas
    def detectarEmocaoEIdade(self):
        resultado = DeepFace.analyze(self.frameAtual, actions=['age', 'emotion'], enforce_detection = False, silent = True)

        idade = resultado[0]['age']
        emocao = resultado[0]['dominant_emotion']
        #Switch Case para traduzir emoções para PT-BR
        if emocao == 'angry':
            emocao = 'Raiva'
        elif emocao == 'fear':
            emocao = 'Medo'
        elif emocao == 'neutral':
            emocao = 'Neutro'
        elif emocao == 'sad':
            emocao = 'Tristeza'
        elif emocao == 'disgust':
            emocao = 'Nojo'
        elif emocao == 'happy':
            emocao = 'Feliz'
        elif emocao == 'surprise':
            emocao = 'Surpresa'


        probabilidadeDuvida = self.calcularProbabilidadeDuvida(resultado[0]['emotion'])
        #Altera o limiar de dúvida caso a pessoas seja idosa
        if idade < 60:
            limiarDuvida = 60.00
        elif idade > 60:
            limiarDuvida = 55.00
        #Retorna um boleano para "estaComDuvida" e, se verdadeiro, printa a mensagem
        estaComDuvida = limiarDuvida < probabilidadeDuvida
        if estaComDuvida:
                print("\nx--------------------------------x")
                print("|     Duvida Identificada        |")
                print("x--------------------------------x")

        #Atribui valores aos textos representados na interface tekinter
        self.rotuloEmocao.config(text=f"Emoção: {emocao}")
        self.rotuloIdade.config(text=f"Idade: {idade}")
        self.rotuloProbabilidadeDuvida.config(text=f"Probabilidade de Dúvida: {probabilidadeDuvida:.2f}")

    def calcularProbabilidadeDuvida(self, listaEmocoes):
        #Pesos determinados para cada emoção retornada considerando a interatividade dos pontos observados nessas com os pontos que seriam alterados em caso de             expressão de dúvida 
        pesoEmocoes = {
            'fear': 0.24,
            'angry': 0.19,
            'sad': 0.14,
            'surprise': 0.14,
            'neutral': 0.11,
            'disgust': 0.11,
            'happy': 0.07
        }
        #Calculo da média ponderada dos pesos
        contador = 0
        somaPonderada = 0
        for emocao, peso in pesoEmocoes.items():
            if emocao in listaEmocoes:
                somaPonderada += listaEmocoes[emocao] * peso
                contador += 1

        media = ((somaPonderada / contador)* 25)
        return media
    #Libera a webcam
    def __del__(self):
        self.webcam.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceAssist(root)
    root.mainloop()
