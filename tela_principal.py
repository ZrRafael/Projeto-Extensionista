from tkinter import Toplevel, Label, Button, Tk, font, messagebox

class TelaPrincipal:
    def __init__(self, root, tipo_usuario):
        self.root = root
        self.tipo_usuario = tipo_usuario
        self.toplevel = Toplevel(self.root)
        self.toplevel.title("Sistema de Transporte de Pacientes")
        self.toplevel.geometry("400x400")
        self.toplevel.minsize(400, 400)

        self.fonte_titulo = font.Font(family="Arial", size=16, weight="bold")
        self.fonte_label = font.Font(family="Arial", size=12)
        self.fonte_botao = font.Font(family="Arial", size=12)

        self.toplevel.config(bg="white")

        self.lbl_titulo = Label(self.toplevel, text="Sistema de Transporte de Pacientes", font=self.fonte_titulo, fg="#4682b4", bg="white")
        self.lbl_titulo.pack(pady=10)

        if self.tipo_usuario == "Administrador":
            self.btn_agendamento = Button(self.toplevel, text="Agendamento de Transporte", command=self.abrir_agendamento_admin, font=self.fonte_botao, fg="white", bg="#4682b4")
            self.btn_agendamento.pack(pady=5)
        elif self.tipo_usuario == "Maqueiro":
            self.btn_agendamento = Button(self.toplevel, text="Agendamento de Transporte", command=self.exibir_mensagem_acesso_negado, font=self.fonte_botao, fg="gray", bg="white")
            self.btn_agendamento.pack(pady=5)

        self.btn_solicitacoes = Button(self.toplevel, text="Solicitações de Transporte", command=self.abrir_solicitacoes, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_solicitacoes.pack(pady=5)

        self.btn_prioridades = Button(self.toplevel, text="Gestão de Prioridades", command=self.abrir_gestao_prioridades, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_prioridades.pack(pady=5)

        self.btn_rastreamento = Button(self.toplevel, text="Rastreamento de Pacientes", command=self.abrir_rastreamento, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_rastreamento.pack(pady=5)

        self.btn_incidentes = Button(self.toplevel, text="Registro de Incidentes", command=self.abrir_registro_incidentes, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_incidentes.pack(pady=5)

        self.btn_gestao_incidentes = Button(self.toplevel, text="Gestão de Incidentes", command=self.abrir_gestao_incidentes, font=self.fonte_botao, fg="white", bg="#4682b4")
        self.btn_gestao_incidentes.pack(pady=5)

        self.btn_sair = Button(self.toplevel, text="Sair", command=self.sair, font=self.fonte_botao, fg="white", bg="red")
        self.btn_sair.pack(pady=10)

    def mostrar(self):
        self.toplevel.deiconify()

    def abrir_agendamento_admin(self):
        from tela_agendamento import TelaAgendamento
        TelaAgendamento(self.root)

    def exibir_mensagem_acesso_negado(self):
        messagebox.showinfo("Aviso", "Você não tem permissão para acessar esta funcionalidade.")

    def abrir_solicitacoes(self):
        from solicitacoes import TelaSolicitacoes
        TelaSolicitacoes(self.root)

    def abrir_gestao_prioridades(self):
        from gestao_prioridades import TelaGestaoPrioridades
        TelaGestaoPrioridades(self.root)

    def abrir_rastreamento(self):
        from rastreamento import TelaRastreamento
        TelaRastreamento(self.root)

    def abrir_registro_incidentes(self):
        from registro_incidentes import TelaRegistroIncidentes
        TelaRegistroIncidentes(self.root)

    def abrir_gestao_incidentes(self):
        from gestao_incidentes import TelaGestaoIncidentes
        TelaGestaoIncidentes(self.root)

    def sair(self):
        self.toplevel.destroy()
        self.root.deiconify()

if __name__ == "__main__":
    root = Tk()
    TelaPrincipal(root, "Administrador")
    root.mainloop()
