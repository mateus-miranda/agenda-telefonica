import tkinter as tk
from tkinter import ttk
import crud as crud



class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        #componentes
        self.lbID = tk.Label(win, text = 'ID: ')
        self.lbNome = tk.Label (win, text = 'Nome do contato: ')
        self.lbTelefone = tk.Label (win, text = 'Numero do Telefone: ')
        
        #Campo de Textos
        self.txtID = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtTelefone = tk.Entry()

        #botões
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarTelefone)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarTelefone)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirTelefone)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        #Componente TreeView
        self.dadosColunas = ("Id", "Nome", "Telefone")

        self.treeTelefones = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse', show="headings")
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.treeTelefones.yview)
        self.verscrlbar.pack(side='right', fill='x')
        
        
        #Head
        self.treeTelefones.heading("Id", text="ID")
        self.treeTelefones.heading("Nome", text="Nome")
        self.treeTelefones.heading("Telefone", text="Telefone")

        #Columns
        self.treeTelefones.column("Id", minwidth=0, width=100)
        self.treeTelefones.column("Nome", minwidth=0, width=200)
        self.treeTelefones.column("Telefone", minwidth=0, width=200)
        self.treeTelefones.pack(padx=10, pady=10)

        self.treeTelefones.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        #Posicionamento dos Componentes na Janela
        
        self.lbID.place(x=100, y=50)
        self.txtID.place(x=250, y=50)

        self.lbNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lbTelefone.place(x=100, y=150)
        self.txtTelefone.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeTelefones.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.carregarDadosIniciais()
    
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeTelefones.selection():
            item = self.treeTelefones.item(selection)
            id,nome,telefone = item["values"] [0:3]
            self.txtID.insert(0, id)
            self.txtNome.insert(0, nome)
            self.txtTelefone.insert(0, telefone)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print("***********Dados Disponiveis no BD***********")
            for item in registros:
                id = item[0]
                nome = item[1]
                telefone = item[2]
                print("ID = ", id)
                print("Nome = ", nome)
                print("Telefone = ", telefone)

                self.treeTelefones.insert('', 'end', iid=self.iid, values=(id,nome,telefone))

                self.iid = self.iid + 1
                self.id = self.id + 1
            print("Dados da Base")
        except:
            print("Ainda não existem dados para carregar")

    def fLerCampos(self):
        try:
            print("***********Dados Disponiveis***********")
            id = int(self.txtID.get())
            print("ID", id)
            nome = self.txtNome.get()
            print("Nome", nome)
            telefone = self.txtTelefone.get()
            print("Telefone", telefone)
            print("Leitura dos Dados Com Sucesso!")
        except:
            print("Não foi possivel ler os dados.")
        return id, nome, telefone
    
    def fCadastrarTelefone(self):
        try:
            print("***********Dados Disponiveis***********")
            id, nome, telefone = self.fLerCampos()
            self.objBD.inserirDados(id, nome, telefone)
            self.treeTelefones.insert('', 'end', iid=self.iid, values=(id, nome, telefone))

            self.iid = self.iid + 1
            self.id = self.id + 1

            self.fLimparTela()
            print("Produto Cadastrado com Sucesso!")
        except:
            print("Não foi possivel fazer o cadastro.")

    def fAtualizarTelefone(self):
        try:
            print("***********Dados Disponiveis***********")
            id, nome, telefone = self.fLerCampos()
            self.objBD.atualizarDados(id, nome, telefone)
            #recarregar dados na tela
            self.treeTelefones.delete(*self.treeTelefones.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto Atualizado com Sucesso!")
        except:
            print("Não foi possivel fazer a atualização.")
    
    def fExcluirTelefone(self):
        try:
            print("***********Dados Disponiveis***********")
            id, nome, telefone = self.fLerCampos()
            self.objBD.excluirDados(id)
            self.treeTelefones.delete(*self.treeTelefones.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto Excluido com Sucesso!")
        except:
            print("Não foi possivel fazer a exclusão do Telefone")

    def fLimparTela(self):
        try:
            print("***********Dados Disponiveis***********")
            self.txtID.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtTelefone.delete(0, tk.END)
            print("Campos Limpos!")
        except:
            print("Não foi possivel limpar os campos.")

janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Agenda Telefonica")
janela.geometry("820x600+10+10")
janela.mainloop()