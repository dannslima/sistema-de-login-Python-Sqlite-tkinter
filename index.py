#importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser



#criar Nossa Janela
jan=Tk()
jan.title('DANILO VASCONCELOS')
jan.geometry('600x300')
jan.configure(background = 'white')
jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.9)
jan.iconbitmap(default='icons/LogoIcon.ico')

# CARREGANDO IMAGENS
logo = PhotoImage(file='icons/logo.png')

LeftFrame = Frame(jan, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack (side=LEFT)

RIGHTFrame = Frame(jan, width=390, height=300, bg='MIDNIGHTBLUE', relief='raise')
RIGHTFrame.pack (side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)

UserLabel = Label(RIGHTFrame,text='Login:', font=('Century Gothic',20),bg='MIDNIGHTBLUE', fg='white')
UserLabel.place(x=5,y=80)

UserEntry = ttk.Entry(RIGHTFrame, width=30)
UserEntry.place(x=170,y=90)

PassLabel = Label(RIGHTFrame, text='Senha:', font=('Century Gothic',20),bg='MIDNIGHTBLUE',fg='white')
PassLabel.place(x=5,y=120)

PassEntry = ttk.Entry(RIGHTFrame, width=30, show='*')
PassEntry.place(x=170,y=130)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT User,PASSWORD FROM USERS
    WHERE User = ? and Password = ?;""",(User, Pass))
    print ('selecionou')

    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title='Login Info',message='Acesso confirmado')
    except:
            messagebox.showerror(title='LoginInfo',message='Acesso Negado')

#Botoes
LoginButton = ttk.Button(RIGHTFrame, text='Login',width=20,command=Login)
LoginButton.place(x=105, y=200)

def Register():
    #removendo Widgests de Login
    LoginButton.place(x=7000)
    RegisterButton.place(x=7000)
    #Inserind Widgets de Cadastro
    NomeLabel = Label(RIGHTFrame, text='Nome', font=('Century Gothic',20), bg='MIDNIGHTBLUE', fg='white')
    NomeLabel.place(x=5,y=5)

    NomeEntry = ttk.Entry(RIGHTFrame, width=42)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RIGHTFrame, text='Email', font=('Century Gothic',20), bg="MIDNIGHTBLUE", fg='white')
    EmailLabel.place(x=5,y=45)

    EmailEntry = ttk.Entry(RIGHTFrame, width=42)
    EmailEntry.place(x=100,y=55)

    def Voltar():
        #Removento Widgets de Cadastro
        NomeLabel.place(x=7000)
        NomeEntry.place(x=7000)
        EmailLabel.place(x=7000)
        EmailEntry.place(x=7000)
        VoltarButton.place(x=7000)
        SalvarButton.place(x=7000)
        #trazendo de volta Widgets de login
        LoginButton.place(x=105)
        RegisterButton.place(x=105)
        User = UserEntry.get()
        Pass = PassEntry.get()

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User =  UserEntry.get()
        Pass = PassEntry.get()

        if Name =='' or Email =='' or User == '' or Pass == '':
            messagebox.showerror(title='Campos vazios', message='Insira todos os campos')
        else:
             DataBaser.cursor.execute("""
             INSERT INTO USERS (Name, Email , User, Password) values (?,?,?,?)
                      """, (Name, Email, User, Pass))
             DataBaser.conn.commit()
             messagebox.showinfo(title='Registro', message='Registrado com sucesso')

    SalvarButton = ttk.Button(RIGHTFrame, text='Salvar', width=20, command = RegisterToDataBase)
    SalvarButton.place(x=105,y=240)

    VoltarButton = ttk.Button(RIGHTFrame, text='Voltar', width=20,command=Voltar )
    VoltarButton.place(x=105, y=200)

RegisterButton = ttk.Button(RIGHTFrame, text='Cadastrar', width=20, command=Register)
RegisterButton.place(x=105,y=240)


jan.mainloop()
DataBaser.conn.close()