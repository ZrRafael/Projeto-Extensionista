from tkinter import Toplevel, Label, Button, Text, Scrollbar, Tk, font, messagebox, Listbox, Entry, END
import solicitacoes

class TelaRegistroIncidentes:
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(self.master)
        self.toplevel.title("Registro de Incidentes")
        self.toplevel.geometry("500x400")
        self.toplevel.minsize(500, 400)
        self.toplevel.config(bg="white")

        self.fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
        self.fonte_label = font.Font(family="Arial", size=12)
        self.fonte_botao = font.Font(family="Arial", size=12)

        self.lbl_titulo = Label(self.toplevel, text="Registro de Incidentes", font=self.fonte_titulo, fg="#4682b4", bg="white")
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.lbl_paciente = Label(self.toplevel, text="Selecione o Paciente:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_paciente.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.lista_pacientes = Listbox(self.toplevel, font=self.fonte_label, selectmode="single")
        self.lista_pacientes.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        for solicitacao in solicitacoes.solicitacoes:
            self.lista_pacientes.insert(END, solicitacao["paciente"])

        self.scrollbar = Scrollbar(self.toplevel, command=self.lista_pacientes.yview)
        self.lista_pacientes.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky="ns")

        self.lbl_buscar = Label(self.toplevel, text="Buscar Paciente:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_buscar.grid(row=2, column=0, padx=10, pady=5, sticky="ne")
        self.entry_buscar = Entry(self.toplevel, font=self.fonte_label)
        self.entry_buscar.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        self.lbl_descricao = Label(self.toplevel, text="Descrição do Incidente:", font=self.fonte_label, fg="black", bg="white")
        self.lbl_descricao.grid(row=3, column=0, padx=10, pady=5, sticky="ne")
        self.text_descricao = Text(self.toplevel, height=10, font=self.fonte_label, wrap="word")
        self.text_descricao.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

        self.scrollbar = Scrollbar(self.toplevel, command=self.text_descricao.yview)
        self.text_descricao.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=2, sticky="ns")

        self.btn_registrar = Button(self.toplevel, text="Registrar", command=self.registrar_incidente, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_registrar.grid(row=4, column=0, columnspan=3, pady=10)

        self.toplevel.grid_rowconfigure(3, weight=1)
        self.toplevel.grid_columnconfigure(1, weight=1)

    def registrar_incidente(self):
        if self.lista_pacientes.curselection():
            paciente_selecionado = self.lista_pacientes.get(self.lista_pacientes.curselection()[0])
        else:
            paciente_selecionado = self.entry_buscar.get().strip()

        if paciente_selecionado:
            descricao = self.text_descricao.get("1.0", END).strip()
            
            if descricao:
                solicitacoes.adicionar_incidente(paciente_selecionado, descricao)
                self.lista_pacientes.selection_clear(0, END)
                self.entry_buscar.delete(0, END)
                self.text_descricao.delete("1.0", END)
                print(f"Incidente registrado: Paciente {paciente_selecionado}, Descrição {descricao}")
            else:
                messagebox.showerror("Erro", "Por favor, preencha a descrição do incidente.")
        else:
            messagebox.showerror("Erro", "Por favor, selecione ou busque um paciente.")

    def mostrar(self):
        self.toplevel.deiconify()

if __name__ == "__main__":
    root = Tk()
    TelaRegistroIncidentes(root)
    root.mainloop()
