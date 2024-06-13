from tkinter import Toplevel, Label, Listbox, Button, END, Tk, font
import solicitacoes

class TelaGestaoIncidentes:
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(self.master)
        self.toplevel.title("Gestão de Incidentes")
        self.toplevel.geometry("500x400")
        self.toplevel.minsize(500, 400)
        self.toplevel.config(bg="white")

        self.fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
        self.fonte_label = font.Font(family="Arial", size=12)
        self.fonte_botao = font.Font(family="Arial", size=12)

        self.lbl_titulo = Label(self.toplevel, text="Gestão de Incidentes", font=self.fonte_titulo, fg="#4682b4", bg="white")
        self.lbl_titulo.pack(pady=10)

        self.lbl_incidentes = Label(self.toplevel, text="Incidentes Registrados", font=self.fonte_label, fg="black", bg="white")
        self.lbl_incidentes.pack()

        self.listbox_incidentes = Listbox(self.toplevel, font=self.fonte_label)
        self.listbox_incidentes.pack(fill="both", expand=True)

        self.btn_atualizar = Button(self.toplevel, text="Atualizar", command=self.atualizar_incidentes, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_atualizar.pack(pady=10)

        self.atualizar_incidentes()

    def atualizar_incidentes(self):
        self.listbox_incidentes.delete(0, END)
        
        for incidente in solicitacoes.incidentes:
            self.listbox_incidentes.insert(END, f"Paciente: {incidente['paciente']} - Descrição: {incidente['descricao']}")

if __name__ == "__main__":
    root = Tk()
    TelaGestaoIncidentes(root)
    root.mainloop()
