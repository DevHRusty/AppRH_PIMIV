import customtkinter        #importando a biblioteca
from tkinter import *       #importando a biblioteca

janela = customtkinter.CTk()    #criar a nossa janela

class Aplicativo():             #nome da classe
    def __init__(self):         #todas as classes que chamamos
        self.janela=janela      
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()       #rodar a janela

#modo tela preta 
    def tema(self):
        customtkinter.set_appearance_mode("dark") 

#customizar a janela
    def tela(self):
        janela.title("Aplicativo de RH")        #titulo do app
        janela.geometry("393x852")              #tamanho do app
        janela.resizable(False,False)           #deixar tamanho dele fixo
        janela.iconbitmap("rh.ico")             #icone na janela

#Tela de Login
    def tela_login(self):
        img = PhotoImage(file="rh.png")     #imagem do rh
        img_App = customtkinter.CTkLabel(master=janela, image=img, text="").place(x=69, y=140)        #definindo o local onde a imagem vai ficar                                                                                                    
        text_usuario = customtkinter.CTkLabel(master=janela, text="Usuario").place(x=43, y=315)        #colocar a palavra usuario e onde ela vai ficar                                                                                                     
        entry_usuario = customtkinter.CTkEntry(master=janela, width=336, height=67, corner_radius=100).place(x=26, y=341)     #caixa para escrever o usuario e aonde ela vai ficar                                                                                                       
        text_senha = customtkinter.CTkLabel(master=janela, text="Senha").place(x=43, y=458)      #colocar a palavra senha e onde ela vai ficar                                                                       
        entry_senha = customtkinter.CTkEntry(master=janela, placeholder_text="", show="*", width=336, height=67, corner_radius=100).place(x=26, y=484)     #caixa para escrever a senha e aonde ela vai ficar                                                                                                            
        Checkbox = customtkinter.CTkCheckBox(master=janela, width=30, height=30, corner_radius=5, text="lembrar da proxima vez" ).place(x=40, y=580)        #checkbox e aonde ela vai ficar
        btnEntrar = customtkinter.CTkButton(master=janela, width= 195, height=48, corner_radius= 100, text="Entrar", font=("ariel", 30)).place(x=93, y=655)     #botao de efetuar login e aonde vai ficar                                                                                                       
        text_EsqSenha = customtkinter.CTkLabel(master=janela, width=136, height=17, text= "Esqueci a senha").place(x=123, y=716)     #botao esqueci a senha e aonde vai ficar                                                                                                     



Aplicativo()


