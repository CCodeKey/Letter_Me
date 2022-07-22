from cgitb import text
import logging
from shutil import which
from tkinter import * 
from tkinter import messagebox
from h11 import InformationalResponse
import pyautogui as p
import socket
from setuptools import Command
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime
# AREA DE LOGIN
def Login():
        senhas = {
            "tt4g" : 202016610015,
            "t001" : 202116610019,
            "trrt" : 202116610022,
        }
        IP_Servidor = "10.15.2.98"
        p.hotkey('alt','f4')
        pop = Tk()
        pop.title(" Login ")
        pop.geometry('300x250')
        def recebimento():
                    MINHA_PORTA = 5100
                    MEU_SERVIDOR = (IP_Servidor, MINHA_PORTA)
                    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                    udp.bind(MEU_SERVIDOR)
                    mensagem, END_cliente_2 = udp.recvfrom(1024) 
                    print("",END_cliente_2)     
                    mensagem = mensagem.decode() 
                    final = str(mensagem)
                    final = final.replace("'","")
                    final = final.replace('"',"")
                    print("==========| ", final ," |==========")
                    messagebox.showinfo("MENSAGENS",final)
                    udp.close()
        def loger():
                    Id = str(senha.get())
                    matricula = senhas.get(Id)
                    if senhas.get(Id):
                        PORTA_Servidor = 5007
                        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        DESTINO = ("10.15.2.98", PORTA_Servidor)
                        udp.sendto (bytes( str(matricula) ,"utf8"), DESTINO)
                        Label(pop, text='Logado', bg='#008000', fg='#ffffff', font='Candara 12').place(x=75, y=130, width=150,height=50)
                        recebimento()
                        udp.close()	
                    else:
                            Label(pop, text='Senha não definida', bg='#FF0000', fg='#ffffff', font='Candara 12').place(x=75, y=130, width=150,height=50)
        Label(pop, text='Senha', bg='#ffffff', fg='#000000', font='Candara 12').place(x=100, y=50, width=100,height=20)
        senha = Entry(pop, show='*', relief='flat')# , show="*"
        senha.place(x=20, y=80, width= 260, height=30)
        Button(pop, command=loger, width=10, height=1, text='Entrar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=10, y=210)
        Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=190, y=210)
# AREIA INICIAL
def inicio(): 
    pop = Tk()
    pop.title(" Letter Me ")
    pop.geometry('300x250')
    Button(pop, command=Login, width=20, height=2, text='Login', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=50, y=40)
    Button(pop, command=curso, width=20, height=2, text='Enviar mensagem', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=50, y=105)
    Button(pop, command=sair, width=20, height=2, text='Sair', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=50, y=169)
# AREA DE ENVIO DE MESAGENS
def curso():
        p.hotkey('alt','f4')
        pop = Tk()
        pop.title(" Curso ")
        pop.geometry('300x250')
        def imformatica():
#       1 ano de Informática
                def ano1():
                    p.hotkey('alt','f4')
                    pop = Tk()
                    pop.title(" Curso ")
                    pop.geometry('400x400')
                    label = ttk.Label(text="Selecione Discente ")
                    label.pack(fill=tk.X, padx=20, pady=10)
                    selected_month = tk.StringVar()
                    month_cb = ttk.Combobox(pop, textvariable=selected_month)
                    lista = ['Fulano','Beutrano','Sicrano']
                    month_cb['values'] = [lista[m] for m in range(len(lista))]
                    month_cb['state'] = 'readonly'
                    month_cb.pack(fill=tk.X, padx=10, pady=5)
                    dic = {
                            "Fulano" : 202016610015,
                            "Beutrano" : 202116610019,
                            "Sicrano" : 202116610029
                    }
                    def month_changed(event):
                        def enviarMensagem():
                            IP_Servidor = "10.15.2.98"
                            PORTA_Servidor = 5000 
                            PORTA_Servidor2 = 5001
                            udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            DESTINO = (IP_Servidor, PORTA_Servidor)
                            DESTINO2 = (IP_Servidor, PORTA_Servidor2)
                            x = texto.get()
                            udp.sendto (bytes(str(mat),"utf8"), DESTINO) 
                            udp2.sendto (bytes(str(x),"utf8"), DESTINO2)
                            messagebox.showinfo("AVISO","Mensagem Enviada")
                            udp.close()
                            udp2.close()
                        print(selected_month.get())
                        var  = selected_month.get()
                        if dic.get(var):
                            mat = dic.get(var)
                            Button(pop, command=enviarMensagem, width=10, height=1, text='Enviar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=185, y=360)
                            print(mat)
                    month_cb.bind('<<ComboboxSelected>>', month_changed)
                    month_cb.set("Discentes")
                    Label(pop, text='Digite uma Mensagem', font='Candara 12').place(x=30, y=83)
                    texto = Text(pop, relief='flat')
                    texto.place(x=20, y=120, width= 360, height=230)
                    Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=294, y=360)
#       2 ano de Informática
                def ano2():
                        p.hotkey('alt','f4')
                        pop = Tk()
                        pop.title(" Curso ")
                        pop.geometry('400x400')
                        label = ttk.Label(text="Selecione Discente ")
                        label.pack(fill=tk.X, padx=20, pady=10)
                        selected_month = tk.StringVar()
                        month_cb = ttk.Combobox(pop, textvariable=selected_month)
                        lista = ['Gabriel de Freitas Tertuliano','Hellen Lima de Araújo','Júlia de Araújo']
                        month_cb['values'] = [lista[m] for m in range(len(lista))]
                        month_cb['state'] = 'readonly'
                        month_cb.pack(fill=tk.X, padx=10, pady=5)
                        dic = {
                                "Gabriel de Freitas Tertuliano" : 202016610015,
                                "Hellen Lima de Araújo" : 202116610019,
                                "Júlia de Araújo" : 202116610029
                        }
                        def month_changed(event):
                            def enviarMensagem():
                                IP_Servidor = "10.15.2.98"
                                PORTA_Servidor = 5000 
                                PORTA_Servidor2 = 5001
                                udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                DESTINO = (IP_Servidor, PORTA_Servidor)
                                DESTINO2 = (IP_Servidor, PORTA_Servidor2)
                                # x = texto.get()
                                x = texto.get('1.0', '10000.0')
                                print('Mensagem: ',x)

                                udp.sendto (bytes(str(mat),"utf8"), DESTINO) 
                                udp2.sendto (bytes(str(x),"utf8"), DESTINO2)
                                messagebox.showinfo("AVISO","Mensagem Enviada")
                                udp.close()
                                udp2.close()
                            print(selected_month.get())
                            var  = selected_month.get()
                            if dic.get(var):
                                mat = dic.get(var)
                                Button(pop, command=enviarMensagem, width=10, height=1, text='Enviar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=185, y=360)
                                print(mat)
                        month_cb.bind('<<ComboboxSelected>>', month_changed)
                        month_cb.set("Discentes")
                        Label(pop, text='Digite uma Mensagem', font='Candara 12').place(x=30, y=83)
                        texto = Text(pop, relief='flat')
                        texto.place(x=20, y=120, width= 360, height=230)
                        Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=294, y=360)
#       3 ano de Informática
                def ano3():
                    p.hotkey('alt','f4')
                    pop = Tk()
                    pop.title(" Curso ")
                    pop.geometry('400x400')
                    label = ttk.Label(text="Selecione Discente ")
                    label.pack(fill=tk.X, padx=20, pady=10)
                    selected_month = tk.StringVar()
                    month_cb = ttk.Combobox(pop, textvariable=selected_month)
                    lista = ['Fulano','Beutrano','Sicrano']
                    month_cb['values'] = [lista[m] for m in range(len(lista))]
                    month_cb['state'] = 'readonly'
                    month_cb.pack(fill=tk.X, padx=10, pady=5)
                    dic = {
                            "Fulano" : 202016610015,
                            "Beutrano" : 202116610019,
                            "Júlia de Araújo" : 202116610029
                    }
                    def month_changed(event):
                        def enviarMensagem():
                            IP_Servidor = "10.15.2.98"
                            PORTA_Servidor = 5000 
                            PORTA_Servidor2 = 5001
                            udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            DESTINO = (IP_Servidor, PORTA_Servidor)
                            DESTINO2 = (IP_Servidor, PORTA_Servidor2)
                            x = texto.get()
                            udp.sendto (bytes(str(mat),"utf8"), DESTINO) 
                            udp2.sendto (bytes(str(x),"utf8"), DESTINO2)
                            messagebox.showinfo("AVISO","Mensagem Enviada")
                            udp.close()
                            udp2.close()
                        print(selected_month.get())
                        var  = selected_month.get()
                        if dic.get(var):
                            mat = dic.get(var)
                            Button(pop, command=enviarMensagem, width=10, height=1, text='Enviar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=185, y=360)
                            print(mat)
                    month_cb.bind('<<ComboboxSelected>>', month_changed)
                    month_cb.set("Discentes")
                    Label(pop, text='Digite uma Mensagem', font='Candara 12').place(x=30, y=83)
                    texto = Text(pop, relief='flat')
                    texto.place(x=20, y=120, width= 360, height=230)
                    Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=294, y=360)
#       Séries {Informática} / 1    / 2    / 3
                Label(pop, width=500, height=600, fg='#ffffff', bg='#f5f5f5').place(x=0, y=0)
                Button(pop, command=ano1, width=10, height=2, text='1° Ano', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=40, y=40)
                Button(pop, command=ano2, width=10, height=2, text='2° Ano', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=40, y=110)
                Button(pop, command=ano3, width=10, height=2, text='3° Ano', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=160, y=70)
                Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=190, y=210)
        def edificacao():
#           1 ano de Edificações
                def ano1():
                        p.hotkey('alt','f4')
                        pop = Tk()
                        pop.title(" Curso ")
                        pop.geometry('400x400')
                        label = ttk.Label(text="Selecione Discente ")
                        label.pack(fill=tk.X, padx=20, pady=10)
                        selected_month = tk.StringVar()
                        month_cb = ttk.Combobox(pop, textvariable=selected_month)
                        lista = ['Fulano','Beutrano','Sicrano']
                        month_cb['values'] = [lista[m] for m in range(len(lista))]
                        month_cb['state'] = 'readonly'
                        month_cb.pack(fill=tk.X, padx=10, pady=5)
                        dic = {
                                "Fulano" : 202016610015,
                                "Beutrano" : 202116610019,
                                "Sicrano" : 202116610029
                        }
                        def month_changed(event):
                            def enviarMensagem():
                                IP_Servidor = "10.15.2.98"
                                PORTA_Servidor = 5000 
                                PORTA_Servidor2 = 5001
                                udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                DESTINO = (IP_Servidor, PORTA_Servidor)
                                DESTINO2 = (IP_Servidor, PORTA_Servidor2)
                                x = texto.get()
                                udp.sendto (bytes(str(mat),"utf8"), DESTINO) 
                                udp2.sendto (bytes(str(x),"utf8"), DESTINO2)
                                messagebox.showinfo("AVISO","Mensagem Enviada")
                                udp.close()
                                udp2.close()
                            print(selected_month.get())
                            var  = selected_month.get()
                            if dic.get(var):
                                mat = dic.get(var)
                                Button(pop, command=enviarMensagem, width=10, height=1, text='Enviar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=185, y=360)
                                print(mat)
                        month_cb.bind('<<ComboboxSelected>>', month_changed)
                        month_cb.set("Discentes")
                        Label(pop, text='Digite uma Mensagem', font='Candara 12').place(x=30, y=83)
                        texto = Text(pop, relief='flat')
                        texto.place(x=20, y=120, width= 360, height=230)
                        Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=294, y=360)
   #           2 ano de Edificações
                def ano2():
                            p.hotkey('alt','f4')
                            pop = Tk()
                            pop.title(" Curso ")
                            pop.geometry('400x400')
                            label = ttk.Label(text="Selecione Discente ")
                            label.pack(fill=tk.X, padx=20, pady=10)
                            selected_month = tk.StringVar()
                            month_cb = ttk.Combobox(pop, textvariable=selected_month)
                            lista = ['Fulano','Beutrano','Sicrano']
                            month_cb['values'] = [lista[m] for m in range(len(lista))]
                            month_cb['state'] = 'readonly'
                            month_cb.pack(fill=tk.X, padx=10, pady=5)
                            dic = {
                                    "Fulano" : 202016610015,
                                    "Beutrano" : 202116610019,
                                    "Sicrano" : 202116610029
                            }
                            def month_changed(event):
                                def enviarMensagem():
                                    IP_Servidor = "10.15.2.98"
                                    PORTA_Servidor = 5000 
                                    PORTA_Servidor2 = 5001
                                    udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                    DESTINO = (IP_Servidor, PORTA_Servidor)
                                    DESTINO2 = (IP_Servidor, PORTA_Servidor2)
                                    x = texto.get()
                                    udp.sendto (bytes(str(mat),"utf8"), DESTINO) 
                                    udp2.sendto (bytes(str(x),"utf8"), DESTINO2)
                                    messagebox.showinfo("AVISO","Mensagem Enviada")
                                    udp.close()
                                    udp2.close()
                                print(selected_month.get())
                                var  = selected_month.get()
                                if dic.get(var):
                                    mat = dic.get(var)
                                    Button(pop, command=enviarMensagem, width=10, height=1, text='Enviar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=185, y=360)
                                    print(mat)
                            month_cb.bind('<<ComboboxSelected>>', month_changed)
                            month_cb.set("Discentes")
                            Label(pop, text='Digite uma Mensagem', font='Candara 12').place(x=30, y=83)
                            texto = Text(pop, relief='flat')
                            texto.place(x=20, y=120, width= 360, height=230)
                            Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=294, y=360)
#           3 ano de Edificações
                def ano3():
                        p.hotkey('alt','f4')
                        pop = Tk()
                        pop.title(" Curso ")
                        pop.geometry('400x400')
                        label = ttk.Label(text="Selecione Discente ")
                        label.pack(fill=tk.X, padx=20, pady=10)
                        selected_month = tk.StringVar()
                        month_cb = ttk.Combobox(pop, textvariable=selected_month)
                        lista = ['Fulano','Beutrano','Sicrano']
                        month_cb['values'] = [lista[m] for m in range(len(lista))]
                        month_cb['state'] = 'readonly'
                        month_cb.pack(fill=tk.X, padx=10, pady=5)
                        dic = {
                                "Fulano" : 202016610015,
                                "Beutrano" : 202116610019,
                                "Sicrano" : 202116610029
                        }
                        def month_changed(event):
                            def enviarMensagem():
                                IP_Servidor = "10.15.2.98"
                                PORTA_Servidor = 5000 
                                PORTA_Servidor2 = 5001
                                udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                DESTINO = (IP_Servidor, PORTA_Servidor)
                                DESTINO2 = (IP_Servidor, PORTA_Servidor2)
                                x = texto.get()
                                udp.sendto (bytes(str(mat),"utf8"), DESTINO) 
                                udp2.sendto (bytes(str(x),"utf8"), DESTINO2)
                                messagebox.showinfo("AVISO","Mensagem Enviada")
                                udp.close()
                                udp2.close()
                            print(selected_month.get())
                            var  = selected_month.get()
                            if dic.get(var):
                                mat = dic.get(var)
                                Button(pop, command=enviarMensagem, width=10, height=1, text='Enviar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=185, y=360)
                                print(mat)
                        month_cb.bind('<<ComboboxSelected>>', month_changed)
                        month_cb.set("Discentes")
                        Label(pop, text='Digite uma Mensagem', font='Candara 12').place(x=30, y=83)
                        texto = Text(pop, relief='flat')
                        texto.place(x=20, y=120, width= 360, height=230)
                        Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=294, y=360)
#       Séries {Edificações} / 1    / 2    / 3
                Label(pop, width=500, height=600, fg='#ffffff', bg='#f5f5f5').place(x=0, y=0)
                Button(pop, command=ano1, width=10, height=2, text='1° Ano', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=40, y=40)
                Button(pop, command=ano2, width=10, height=2, text='2° Ano', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=40, y=110)
                Button(pop, command=ano3, width=10, height=2, text='3° Ano', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=160, y=70)
                Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=190, y=210)
    #     Cursos (Informática e Edificações )....
        Button(pop, command=imformatica, width=15, height=2, text='Informática', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=70, y=40)
        Button(pop, command=edificacao, width=15, height=2, text='Edificações', relief='flat', fg='#ffffff', bg='#78aeff', font='Candara 14 bold').place(x=70, y=120)
        Button(pop, command=voltar, width=10, height=1, text='Voltar', relief='flat', fg='#ffffff', bg='#ffb8c1', font='Candara 12 bold').place(x=190, y=210)
########################################################################################################################################################################     

#                                           GATILHOS

######################################################################################################################################################################## 
def sair():
    p.hotkey('alt','f4')
def voltar():
    p.hotkey('alt','f4')
    inicio()
######################################################################################################################################################################## 
inicio()
tk.mainloop()