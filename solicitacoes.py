# solicitacoes.py

from tkinter import Toplevel, Label, Listbox, Button, END
import tkinter as tk
import tkinter.font as font

solicitacoes = []
incidentes = []

def adicionar_solicitacao(paciente, destino_inicial, destino_final, prioridade):
    solicitacoes.append({"paciente": paciente, "destino_inicial": destino_inicial, "destino_final": destino_final, "prioridade": prioridade, "status": "Pendente"})

def adicionar_incidente(paciente, descricao):
    incidentes.append({"paciente": paciente, "descricao": descricao})


class TelaAgendamento:
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(self.master)
        self.toplevel.title("Agendamento de Transporte")
        self.toplevel.geometry("400x400")
        self.toplevel.minsize(400, 400)

        self.fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
        self.fonte_label = font.Font(family="Arial", size=12)
        self.fonte_botao = font.Font(family="Arial", size=12)

        self.toplevel.config(bg="white")

        self.lbl_titulo = Label(self.toplevel, text="Agendamento de Transporte", font=self.fonte_titulo, fg="#4682b4", bg="white")
        self.lbl_titulo.pack(pady=10)

        self.lbl_paciente = Label(self.toplevel, text="Nome do Paciente:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_paciente.pack(pady=5)
        self.entry_paciente = tk.Entry(self.toplevel, font=self.fonte_label)
        self.entry_paciente.pack(pady=5)

        self.lbl_destino_inicial = tk.Label(self.toplevel, text="Destino Inicial:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_destino_inicial.pack(pady=5)
        self.entry_destino_inicial = tk.Entry(self.toplevel, font=self.fonte_label)
        self.entry_destino_inicial.pack(pady=5)

        self.lbl_destino_final = tk.Label(self.toplevel, text="Destino Final:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_destino_final.pack(pady=5)
        self.entry_destino_final = tk.Entry(self.toplevel, font=self.fonte_label)
        self.entry_destino_final.pack(pady=5)

        self.lbl_prioridade = tk.Label(self.toplevel, text="Prioridade:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_prioridade.pack(pady=5)
        self.prioridades = ["Baixa", "Média", "Alta", "Crítica"]
        self.var_prioridade = tk.StringVar(self.toplevel)
        self.var_prioridade.set(self.prioridades[0])
        self.menu_prioridade = tk.OptionMenu(self.toplevel, self.var_prioridade, *self.prioridades)
        self.menu_prioridade.config(font=self.fonte_label, fg="black", bg="#4682b4", highlightbackground="white")
        self.menu_prioridade.pack(pady=5)

        self.btn_agendar = tk.Button(self.toplevel, text="Agendar", command=self.agendar, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_agendar.pack(pady=20)

    def agendar(self):
        paciente = self.entry_paciente.get().strip()
        destino_inicial = self.entry_destino_inicial.get().strip()
        destino_final = self.entry_destino_final.get().strip()
        prioridade = self.var_prioridade.get()

        if not paciente or not destino_inicial or not destino_final:
            tk.messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        adicionar_solicitacao(paciente, destino_inicial, destino_final, prioridade)
        self.entry_paciente.delete(0, 'end')
        self.entry_destino_inicial.delete(0, 'end')
        self.entry_destino_final.delete(0, 'end')
        self.var_prioridade.set(self.prioridades[0])
        print(f"Agendamento: Paciente {paciente}, Destino Inicial {destino_inicial}, Destino Final {destino_final}, Prioridade {prioridade}")

    def mostrar(self):
        self.toplevel.deiconify()


class TelaSolicitacoes:
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(self.master)
        self.toplevel.title("Solicitações de Transporte")
        self.toplevel.geometry("750x650")
        self.toplevel.configure(bg='#F0F8FF')

        self.lbl_solicitacoes = Label(self.toplevel, text="Solicitações de Transporte", font=("Helvetica", 16, "bold"), fg="#4682b4", bg='#F0F8FF')
        self.lbl_solicitacoes.pack(pady=20)

        self.listbox_solicitacoes = Listbox(self.toplevel, font=("Helvetica", 12))
        self.listbox_solicitacoes.pack(fill="both", expand=True, padx=20, pady=10)

        self.btn_aceitar = Button(self.toplevel, text="Aceitar", command=self.aceitar, font=("Helvetica", 12, "bold"), bg='#4682B4', fg='white', activebackground='#5F9EA0')
        self.btn_aceitar.pack(side="left", padx=20, pady=20)

        self.btn_recusar = Button(self.toplevel, text="Recusar", command=self.recusar, font=("Helvetica", 12, "bold"), bg='#4682B4', fg='white', activebackground='#5F9EA0')
        self.btn_recusar.pack(side="right", padx=20, pady=20)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.listbox_solicitacoes.delete(0, END)
        for solicitacao in solicitacoes:
            status = solicitacao.get("status", "Pendente")  
            prioridade = solicitacao["prioridade"]
            self.listbox_solicitacoes.insert(END, f"Paciente: {solicitacao['paciente']} - Destino Inicial: {solicitacao['destino_inicial']} - Destino Final: {solicitacao['destino_final']} - Prioridade: {prioridade} - Status: {status}")

    def aceitar(self):
        selecao = self.listbox_solicitacoes.curselection()
        if selecao:
            index = selecao[0]
            solicitacoes[index]["status"] = "Aceito"
            self.atualizar_lista()

    def recusar(self):
        selecao = self.listbox_solicitacoes.curselection()
        if selecao:
            index = selecao[0]
            solicitacoes[index]["status"] = "Recusado"
            self.atualizar_lista()


if __name__ == "__main__":
    root = tk.Tk()
    TelaAgendamento(root)
    TelaSolicitacoes(root)
    root.mainloop()
