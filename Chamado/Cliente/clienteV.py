import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import socket, json

janela = ctk.CTk()

class Application():
    def __init__(self): 
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("#6B6ABD")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("800x600")
        janela.title("Sistema de registro")
        janela.iconbitmap("")
        janela.resizable(False, False)
        

    def tela_login(self):
        
        # Comuncação entre o servidor
        host = "127.0.1.1" # Deve ter o mesmo ip do servidor.
        port = 55555

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect((host, port))                                    
        except:
            messagebox.showerror("ERROR!!!", "Não foi possível conectar-se ao servidor!")
            return janela.destroy()
            


        #frame
        novot_frame = ctk.CTkFrame(master=janela,  fg_color="#6B6ABD", height=60, width=1024)
        novot_frame.pack(side=TOP)

        cadastro_frame = ctk.CTkFrame(master=janela, fg_color="#E9E8FA", height=1024, width=1024)
        cadastro_frame.pack(side=BOTTOM)

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de ticket:", font=("Inter Bold", 18), text_color="#26248E")
        label.place(x=10, y=15)

        label = ctk.CTkLabel(master=novot_frame, text=" + Novo Ticket", font=("Inter Bold",13), text_color="#FFFFFF")
        label.place(x= 10, y= 15)

        # Variáveis de cada entrada (textvariable)
        name_value = StringVar()
        cpf_value = StringVar()
        cidade_value = StringVar()
        telefone_value = StringVar()
        setor_value = StringVar()
        email_value = StringVar()
        situ_value = StringVar()
        
        # entrada de dados
        nome_entry = ctk.CTkEntry(master=cadastro_frame, textvariable=name_value, placeholder_text="", width=300, font=("Roboto bold",14), fg_color="#6B6ABD",text_color="#FFFFFF")
        nome_entry.place(x=80, y=50)
        nome_label = ctk.CTkLabel(master=cadastro_frame, text="Nome:", text_color="#26248E", font=("Inter Bold", 14))
        nome_label.place(x=8, y=50)

        cpf_entry = ctk.CTkEntry(master=cadastro_frame, textvariable=cpf_value, placeholder_text="", width=300, font=("Roboto bold",14), fg_color="#6B6ABD",  text_color="#FFFFFF")
        cpf_entry.place(x=80, y=80)
        cpf_label = ctk.CTkLabel(master=cadastro_frame, text="CPF:", text_color="#26248E", font=("Inter Bold", 14))
        cpf_label.place(x=8, y=80)

        cidade_entry = ctk.CTkEntry(master=cadastro_frame, textvariable=cidade_value, placeholder_text="", width=300, font=("Roboto bold",14), fg_color="#6B6ABD", text_color="#FFFFFF")
        cidade_entry.place(x=80, y=110)
        cidade_label = ctk.CTkLabel(master=cadastro_frame, text="Cidade:", text_color="#26248E", font=("Inter Bold", 14))
        cidade_label.place(x=8, y=110)

        telefone_entry = ctk.CTkEntry(master=cadastro_frame, textvariable=telefone_value, placeholder_text="", width=300, font=("Roboto bold",14), fg_color="#6B6ABD", text_color="#FFFFFF")
        telefone_entry.place(x=80, y=140)
        telefone_label = ctk.CTkLabel(master=cadastro_frame, text="Telefone:", text_color="#26248E", font=("Inter Bold", 14))
        telefone_label.place(x=8, y=140)

        setor_entry = ctk.CTkEntry(master=cadastro_frame, textvariable=setor_value, placeholder_text="", width=300, font=("Roboto bold",14), fg_color="#6B6ABD", text_color="#FFFFFF")
        setor_entry.place(x=80, y=170)
        setor_label = ctk.CTkLabel(master=cadastro_frame, text="Setor:", text_color="#26248E", font=("Inter Bold", 14))
        setor_label.place(x=8, y=170)

        email_entry = ctk.CTkEntry(master=cadastro_frame, textvariable=email_value, placeholder_text="", width=300, font=("Roboto bold",14), fg_color="#6B6ABD", text_color="#FFFFFF")
        email_entry.place(x=80, y=200)
        email_label = ctk.CTkLabel(master=cadastro_frame, text="E-mail:", text_color="#26248E", font=("Inter Bold", 14))
        email_label.place(x=8, y=200)

        situ_text = ctk.CTkTextbox(master=cadastro_frame, width=300, height=115, font=("Roboto bold",14), fg_color="#6B6ABD", text_color="#FFFFFF",)
        situ_text.place(x=80, y=230)
        situ_label = ctk.CTkLabel(master=cadastro_frame, text="Situação:", text_color="#26248E", font=("Inter Bold", 14))
        situ_label.place(x=8, y=230)
 

        def interacao():
            nome = name_value.get()
            cpf = cpf_value.get()
            cidade = cpf_value.get()
            telefone = telefone_value.get()
            setor = setor_value.get()
            email = email_value.get()
            situacao = situ_text.get(0.0, END)
            
            messagebox.showinfo("Sucesso!", "Sua solicitação foi enviada. Em breve um técnico entrará em contato para realizar o atendimento.")
            janela.destroy()

            # Back-end
            

            def main():

                dados = """
                {
                    "Nome": "nome",
                    "CPF": "cpf",
                    "Cidade": "cidade",
                    "Telefone": "tel",
                    "Setor": "setor",
                    "Email": "email",
                    "Situacao": "situacao"
                }
                """

                

                info = json.loads(dados)
                    
                for i in info:
                    if i == "Nome":
                        info[i] = nome
                    elif i == "CPF":
                        info[i] = cpf
                    elif i == "Cidade":
                        info[i] = cidade
                    elif i == "Telefone":
                        info[i] = telefone
                    elif i == "Setor":
                        info[i] = setor
                    elif i == "Email":
                        info[i] = email  
                    elif i == "Situacao":
                        info[i] = situacao  

                
                with open("bancodados.json", "w") as dAtua:
                    dAtua.write(json.dumps(info, indent=2))
                                                                    #Partes da comunicação do arquivo json e o código
                with open("bancodados.json") as dAtua2:
                    msg = json.load(dAtua2)


                client.send(f' {msg}'.encode())                     #Envio de dados para o servidor
            main()  


        
        
        enviar_button = ctk.CTkButton(master=cadastro_frame, text="Enviar", width=150, fg_color="#26248A", font=("Roboto bold",14), command=interacao)
        enviar_button.place(x=230, y=350)
        
Application()
