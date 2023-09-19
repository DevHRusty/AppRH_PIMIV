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
        login_frame = customtkinter.CTkFrame(master=janela, width=393, height=852).place(x=393, y=852)
        img = PhotoImage(file="rh.png")     #imagem do rh
        img_App = customtkinter.CTkLabel(master=login_frame, image=img, text="").place(x=69, y=140)        #definindo o local onde a imagem vai ficar                                                                                                    
        text_usuario = customtkinter.CTkLabel(master=login_frame, text="Usuario").place(x=43, y=315)        #colocar a palavra usuario e onde ela vai ficar                                                                                                     
        entry_usuario = customtkinter.CTkEntry(master=login_frame, width=336, height=67, corner_radius=100).place(x=26, y=341)     #caixa para escrever o usuario e aonde ela vai ficar                                                                                                       
        text_senha = customtkinter.CTkLabel(master=login_frame, text="Senha").place(x=43, y=458)      #colocar a palavra senha e onde ela vai ficar                                                                       
        entry_senha = customtkinter.CTkEntry(master=login_frame, placeholder_text="", show="*", width=336, height=67, corner_radius=100).place(x=26, y=484)     #caixa para escrever a senha e aonde ela vai ficar                                                                                                            
        Checkbox = customtkinter.CTkCheckBox(master=login_frame, width=30, height=30, corner_radius=5, text="lembrar da proxima vez" ).place(x=40, y=580)        #checkbox e aonde ela vai ficar
        btnEntrar = customtkinter.CTkButton(master=login_frame, width= 195, height=48, corner_radius= 100, text="Entrar", font=("ariel", 30)).place(x=93, y=655)     #botao de efetuar login e aonde vai ficar        
        text_EsqSenha = customtkinter.CTkButton(master=login_frame, width=136, height=10, command=tela_red_senha, corner_radius= 100, text= "Esqueci a senha").place(x=123, y=716)     #botao esqueci a senha e aonde vai ficar                                                                                                    
        
        def tela_red_senha():
            login_frame.pack_forget() #fechar a janela
            red_senha_frame = Frame(master=janela, bg="#01476E",)     
Aplicativo()


