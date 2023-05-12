from tkinter import ttk
from tkinter import *
import pyautogui
pyautogui.PAUSE = 1


janela = Tk()
idades = []
usuarios =[]


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inserts()
        self.lista()
        janela.mainloop()

    def tela(self):
        self.janela.title("NETFLIX")
        self.janela.configure(background="#7c8f8d")
        self.janela.geometry("700x800")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=800)

    def frames(self):
        self.frame0 = Frame(self.janela, bg="#9fcfca")
        self.frame0.place(relheight=0.07, relwidth=0.94, relx=0.03, rely=0.03)
        self.frame1 = Frame(self.janela, bg="#9fcfca")
        self.frame1.place(relheight=0.20, relwidth=0.94, relx=0.03, rely=0.12)
        self.frame2 = Frame(self.janela, bg="#9fcfca")
        self.frame2.place(relheight=0.25, relwidth=0.94, relx=0.03, rely=0.34)

    def botoes(self):
        self.btBuscar = Button(self.frame0, text='Buscar', bg="#7c8f8d")
        self.btBuscar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btLimpar = Button(self.frame0, text='Limpar', bg="#7c8f8d", command=self.limpar_tela)
        self.btLimpar.place(relx=0.27, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btCreate = Button(self.frame0, text='Create', bg="#7c8f8d")
        self.btCreate.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btRead = Button(self.frame0, text='Read', bg="#7c8f8d")
        self.btRead.place(relx=0.57, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btUpdate = Button(self.frame0, text='Update', bg="#7c8f8d")
        self.btUpdate.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btDelete = Button(self.frame0, text='Delete', bg="#7c8f8d")
        self.btDelete.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btDimensao = Button(self.janela, text='Dimensão', bg="#7c8f8d", command=self.dimension)
        self.btDimensao.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.20)

        self.btPosicao = Button(self.janela, text='posição', bg="#7c8f8d", command=self.position)
        self.btPosicao.place(relx=0.20, rely=0.50, relwidth=0.1, relheight=0.10)

        self.btMover = Button(self.janela, text='Mover', bg="#7c8f8d", command=self.move)
        self.btMover.place(relx=0.81, rely=0.50, relwidth=0.1, relheight=0.10)

        self.btAlerta = Button(self.janela, text='Alerta', bg="#7c8f8d", command=self.alert)
        self.btAlerta.place(relx=0.81, rely=0.50, relwidth=0.1, relheight=0.10)

        self.btBot = Button(self.janela, text='Bot', bg="#7c8f8d", command=self.bot)
        self.btBot.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.10)

    def labels(self):
        self.lbIDUsuario = Label(self.frame0, text="ID", background="#7c8f8d")
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.3)

        self.lbNome = Label(self.frame1, text="Nome", bg="#7c8f8d")
        self.lbNome.place(relx=0.005, rely=0.06, relwidth=0.1, relheight=0.15)

        self.lbEmail = Label(self.frame1, text="Email", bg="#7c8f8d")
        self.lbEmail.place(relx=0.005, rely=0.37, relwidth=0.1, relheight=0.15)

        self.lbPlano = Label(self.frame1, text="Plano", bg="#7c8f8d")
        self.lbPlano.place(relx=0.005, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbTipo = Label(self.frame1, text="Tipo", bg="#7c8f8d")
        self.lbTipo.place(relx=0.32, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbIdade = Label(self.frame1, text="Idade", bg="#7c8f8d")
        self.lbIdade.place(relx=0.62, rely=0.69, relwidth=0.1, relheight=0.15)

    def inserts(self):
        self.insertIDUsuario = Entry(self.frame0, background="cyan")
        self.insertIDUsuario.place(relx=0.005, rely=0.40, relwidth=0.1, relheight=0.47)

        self.insertNome = Entry(self.frame1, bg="cyan")
        self.insertNome.place(relx=0.155, rely=0.05, relwidth=0.75, relheight=0.23)

        self.insertEmail = Entry(self.frame1, bg="cyan")
        self.insertEmail.place(relx=0.155, rely=0.37, relwidth=0.75, relheight=0.23)

        self.insertPlano = Entry(self.frame1, bg="cyan")
        self.insertPlano.place(relx=0.155, rely=0.69, relwidth=0.15, relheight=0.23)

        self.insertTipo = Entry(self.frame1, bg="cyan")
        self.insertTipo.place(relx=0.45, rely=0.69, relwidth=0.15, relheight=0.23)

        self.insertIdade = Entry(self.frame1, bg="cyan")
        self.insertIdade.place(relx=0.75, rely=0.69, relwidth=0.15, relheight=0.23)

    def lista(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))

        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Email')
        self.listaCli.heading('#4', text='Plano')
        self.listaCli.heading('#5', text='Tipo')
        self.listaCli.heading('#6', text='Class')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=35)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=188)
        self.listaCli.column('#4', width=70)
        self.listaCli.column('#5', width=70)
        self.listaCli.column('#6', width=70)

        self.listaCli.place(relx=0.025, rely=0.075, relwidth=0.925, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.949, rely=0.079, relwidth=0.02, relheight=0.84)

    def limpar_tela(self):
        self.insertIDUsuario.delete(0, END)
        self.insertNome.delete(0, END)
        self.insertEmail.delete(0, END)
        self.insertPlano.delete(0, END)
        self.insertTipo.delete(0, END)
        self.insertIdade.delete(0, END)

    def dimension(self):
        x, y = pyautogui.size()
        print(x)
        print(y)

    def position(self):
        w, z = pyautogui.position()
        print(w)
        print(z)

    def move(self):
        pyautogui.moveTo(50, 50)

    def alert(self):
        print(pyautogui.confirm(text='Prometo fazer os exercícios', title='Feriado', ))

    def bot(self):
        pyautogui.press('win')
        pyautogui.write('block')
        pyautogui.press('Enter')
        pyautogui.write('Aula de PyautoGUI')
        pyautogui.hotkey('ctrl', 's')
        for i in range(10):
            pyautogui.press('tab')
        for i in range(6):
            pyautogui.press('down')
            pyautogui.press('alt')
        pyautogui.write('rascunho')
        pyautogui.hotkey('alt', 'l')
        pyautogui.hotkey('win', 'd')

