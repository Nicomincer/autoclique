import time
import pyautogui 
import tkinter 



class Aplicação():
     x = 0
     def __init__(self):
          self.valor = False
          self.janela = tkinter.Tk()
          self.janela.geometry("300x50")
          self.botao_iniciar = tkinter.Button(self.janela, text="START", command=self.clicar, width=20)
          self.botao_iniciar.place(relx=0.01, rely=0.5)
          self.botao_parar = tkinter.Button(self.janela, text="STOP", command='', width=20)
          self.botao_parar.place(relx=0.5, rely=0.5)
          self.janela.mainloop()
     def clicar(self):
          self.valor = True
          self.passado = time.localtime()[5]
          self.atual = time.localtime()[5]
          while self.valor:
               pyautogui.click()
               self.janela.mainloop()
     def parar(self):
          print('Parou')
          


if __name__ == "__main__":
     app = Aplicação()