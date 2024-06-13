from tkinter import Toplevel, Label, Entry, Button, StringVar, OptionMenu, Tk, font, messagebox
import solicitacoes

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
        self.entry_paciente = Entry(self.toplevel, font=self.fonte_label)
        self.entry_paciente.pack(pady=5)

        self.lbl_destino_inicial = Label(self.toplevel, text="Destino Inicial:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_destino_inicial.pack(pady=5)
        self.entry_destino_inicial = Entry(self.toplevel, font=self.fonte_label)
        self.entry_destino_inicial.pack(pady=5)

        self.lbl_destino_final = Label(self.toplevel, text="Destino Final:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_destino_final.pack(pady=5)
        self.entry_destino_final = Entry(self.toplevel, font=self.fonte_label)
        self.entry_destino_final.pack(pady=5)

        self.lbl_prioridade = Label(self.toplevel, text="Prioridade:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_prioridade.pack(pady=5)
        self.prioridades = ["Baixa", "Média", "Alta", "Crítica"]
        self.var_prioridade = StringVar(self.toplevel)
        self.var_prioridade.set(self.prioridades[0])
        self.menu_prioridade = OptionMenu(self.toplevel, self.var_prioridade, *self.prioridades)
        self.menu_prioridade.config(font=self.fonte_label, fg="white", bg="#4682b4", highlightbackground="white")
        self.menu_prioridade.pack(pady=5)

        self.btn_agendar = Button(self.toplevel, text="Agendar", command=self.agendar, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_agendar.pack(pady=20)

    def agendar(self):
        paciente = self.entry_paciente.get().strip()
        destino_inicial = self.entry_destino_inicial.get().strip()
        destino_final = self.entry_destino_final.get().strip()
        prioridade = self.var_prioridade.get()

        if not paciente or not destino_inicial or not destino_final:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        solicitacoes.adicionar_solicitacao(paciente, destino_inicial, destino_final, prioridade)
        self.entry_paciente.delete(0, 'end')
        self.entry_destino_inicial.delete(0, 'end')
        self.entry_destino_final.delete(0, 'end')
        self.var_prioridade.set(self.prioridades[0])
        print(f"Agendamento: Paciente {paciente}, Destino Inicial {destino_inicial}, Destino Final {destino_final}, Prioridade {prioridade}")

    def mostrar(self):
        self.toplevel.deiconify()

if __name__ == "__main__":
    root = Tk()
    TelaAgendamento(root)
    root.mainloop()
