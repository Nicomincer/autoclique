import pyautogui 
import tkinter 
import keyboard
import threading
from time import time, sleep


class Aplicação():
    def __init__(self):
        self.rodando = False
        self.janela = tkinter.Tk()
        self.janela.geometry("300x50")
        self.janela.title("Autoclick")
        self.botao_iniciar = tkinter.Button(self.janela, text="START", command=self.clicar, width=20)
        self.botao_iniciar.place(relx=0.01, rely=0.5)
        self.botao_parar = tkinter.Button(self.janela, text="STOP", command=self.parar, width=20)
        self.botao_parar.place(relx=0.5, rely=0.5)
        self.janela.mainloop()

    def clicar(self):
        if self.rodando:
            return
        self.rodando = True
        th_loop_click = threading.Thread(target=self.loop_click)
        th_loop_click.start()

    def loop_click(self):        
        tempo_limite = time() + 30
        while time() < tempo_limite and self.rodando:
               sleep(0.05)
               pyautogui.click()
               if keyboard.is_pressed("n"):
                    self.parar()
          
        self.rodando = False

    def parar(self):
        self.rodando = False
          

if __name__ == "__main__":
     app = Aplicação()