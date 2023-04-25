import pyautogui 
import tkinter 
import keyboard
import threading
from time import sleep


class Aplicação():
    def __init__(self, tecla="n"):
        self.tecla = tecla
        self.rodando = False
        self.janela = tkinter.Tk()
        self.janela.geometry("300x50")
        self.janela.title("Autoclick")
        self.botao_iniciar = tkinter.Button(self.janela, text="START", command=self.clicar, width=20)
        self.botao_iniciar.place(relx=0.01, rely=0.5)
        self.botao_parar = tkinter.Button(self.janela, text="STOP", command=self.parar, width=20)
        self.botao_parar.place(relx=0.5, rely=0.5)
        self.barra_de_menus = tkinter.Menu(self.janela)
        self.menu1 = tkinter.Menu(self.barra_de_menus, tearoff=False)
        self.menu1.add_command(label="Input to Stop", command=self.button)
        self.menu1.add_command(label="")
        self.barra_de_menus.add_cascade(label="Keyboard", menu=self.menu1)
        self.janela.config(menu=self.barra_de_menus)

        self.janela.mainloop()

    def clicar(self):
        if self.rodando:
            return
        self.rodando = True
        th_loop_click = threading.Thread(target=self.loop_click)
        th_loop_click.start()

    def loop_click(self):        

        while self.rodando:
               sleep(0.05)
               pyautogui.click()
               if keyboard.is_pressed(self.tecla):
                    self.parar()
          
        self.rodando = False

    def parar(self):
        self.rodando = False
    
    def button(self):
        self.texto = tkinter.Label(self.janela, text="Stop Button", font=('arial', 10))
        self.texto.place(relx=0, rely=0)
        self.entrada = tkinter.Entry(self.janela, width=10)
        self.entrada.place(relx=0.3, rely=0)
        self.botaoadd = tkinter.Button(self.janela, text="ADD", command=self.mudar_button)
        self.botaoadd.place(relx=0.5, rely=0)
    
    def mudar_button(self):
        self.tecla = self.entrada.get()

if __name__ == "__main__":
    app = Aplicação()