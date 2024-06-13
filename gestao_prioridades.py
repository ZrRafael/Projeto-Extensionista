from tkinter import Toplevel, Label, Listbox, Button, END, Tk, font

import solicitacoes

class TelaGestaoPrioridades:
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(self.master)
        self.toplevel.title("Gestão de Prioridades")
        self.toplevel.geometry("500x400")
        self.toplevel.minsize(500, 400)
        self.toplevel.config(bg="white")

        self.fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
        self.fonte_label = font.Font(family="Arial", size=12)
        self.fonte_botao = font.Font(family="Arial", size=12)

        self.lbl_titulo = Label(self.toplevel, text="Gestão de Prioridades", font=self.fonte_titulo, fg="#4682b4", bg="white")
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.listbox_prioridades = Listbox(self.toplevel, font=self.fonte_label)
        self.listbox_prioridades.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 0), sticky="nsew")

        self.btn_atualizar = Button(self.toplevel, text="Atualizar", command=self.atualizar_prioridades, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_atualizar.grid(row=2, column=0, columnspan=2, pady=10)

        self.atualizar_prioridades()

        self.toplevel.grid_rowconfigure(1, weight=1)
        self.toplevel.grid_columnconfigure(0, weight=1)
        self.toplevel.grid_columnconfigure(1, weight=1)

    def atualizar_prioridades(self):
        prioridades_ordem = {"Crítica": 3, "Alta": 2, "Média": 1, "Baixa": 0}
        solicitacoes.solicitacoes.sort(key=lambda x: prioridades_ordem[x["prioridade"]], reverse=True)

        self.listbox_prioridades.delete(0, END)
        for solicitacao in solicitacoes.solicitacoes:
            self.listbox_prioridades.insert(END, f"Paciente: {solicitacao['paciente']} - Prioridade: {solicitacao['prioridade']}")

    def mostrar(self):
        self.toplevel.deiconify()

if __name__ == "__main__":
    root = Tk()
    TelaGestaoPrioridades(root)
    root.mainloop()
