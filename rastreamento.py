from tkinter import Toplevel, Label, Entry, Button, StringVar, Listbox, Scrollbar, END, Tk, font
import solicitacoes

class TelaRastreamento:
    def __init__(self, master):
        self.master = master
        self.toplevel = Toplevel(self.master)
        self.toplevel.title("Rastreamento de Pacientes")

        self.fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
        self.fonte_instrucao = font.Font(family="Arial", size=12)
        self.fonte_resultado = font.Font(family="Arial", size=14)

        self.lbl_titulo = Label(self.toplevel, text="Rastreamento de Pacientes", font=self.fonte_titulo, fg="#4682B4")
        self.lbl_titulo.pack(pady=10)

        self.lbl_instrucao = Label(self.toplevel, text="Escolha um paciente para rastrear:", font=self.fonte_instrucao)
        self.lbl_instrucao.pack(pady=5)

        self.listbox_pacientes = Listbox(self.toplevel, width=40, font=self.fonte_instrucao)
        self.listbox_pacientes.pack(pady=5, expand=True, fill="both")

        self.scrollbar = Scrollbar(self.toplevel, orient="vertical")
        self.scrollbar.config(command=self.listbox_pacientes.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox_pacientes.config(yscrollcommand=self.scrollbar.set)

        self.btn_rastrear_selecionado = Button(self.toplevel, text="Rastrear Selecionado", command=self.rastrear_selecionado, font=self.fonte_instrucao, fg="white", bg="#4682B4")
        self.btn_rastrear_selecionado.pack(pady=5)

        self.lbl_nome = Label(self.toplevel, text="OU Digite o Nome do Paciente:", font=self.fonte_instrucao)
        self.lbl_nome.pack(pady=5)
        self.entry_nome = Entry(self.toplevel, width=30, font=self.fonte_instrucao)
        self.entry_nome.pack(pady=5)

        self.btn_rastrear_nome = Button(self.toplevel, text="Rastrear por Nome", command=self.rastrear_por_nome, font=self.fonte_instrucao, fg= "white", bg="#4682B4")
        self.btn_rastrear_nome.pack(pady=5)

        self.resultado = StringVar()
        self.lbl_resultado = Label(self.toplevel, textvariable=self.resultado, font=self.fonte_resultado, fg="#4682B4")
        self.lbl_resultado.pack(pady=10)

        self.atualizar_lista_pacientes()

    def atualizar_lista_pacientes(self):
        self.listbox_pacientes.delete(0, END)
        for solicitacao in solicitacoes.solicitacoes:
            self.listbox_pacientes.insert(END, solicitacao["paciente"])

    def rastrear_selecionado(self):
        selecionado = self.listbox_pacientes.curselection()
        if selecionado:
            paciente_selecionado = self.listbox_pacientes.get(selecionado)
            paciente = next((p for p in solicitacoes.solicitacoes if p["paciente"] == paciente_selecionado), None)
            if paciente:
                destino_inicial = paciente.get("destino_inicial", "Não especificado")
                destino_final = paciente.get("destino_final", "Não especificado")
                self.resultado.set(f"Destino Inicial: {destino_inicial} - Destino Final: {destino_final} - Status: {paciente['status']}")
            else:
                self.resultado.set("Paciente não encontrado.")
        else:
            self.resultado.set("Nenhum paciente selecionado.")

    def rastrear_por_nome(self):
        nome = self.entry_nome.get().strip().lower()
        paciente = next((p for p in solicitacoes.solicitacoes if p["paciente"].lower() == nome), None)
        if paciente:
            destino_inicial = paciente.get("destino_inicial", "Não especificado")
            destino_final = paciente.get("destino_final", "Não especificado")
            self.resultado.set(f"Destino Inicial: {destino_inicial} - Destino Final: {destino_final} - Status: {paciente['status']}")
        else:
            self.resultado.set("Paciente não encontrado.")

    def mostrar(self):
        self.toplevel.deiconify()

if __name__ == "__main__":
    root = Tk()
    TelaRastreamento(root)
    root.mainloop()
