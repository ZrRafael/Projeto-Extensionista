from tkinter import Tk, Label, Button, Entry, messagebox
from tkinter.font import Font
from tela_principal import TelaPrincipal

class Sistema:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x320")
        self.root.configure(bg="#f0f0f0")  

        self.fonte_titulo = Font(family="Arial", size=16, weight="bold")
        self.fonte_label = Font(family="Arial", size=12)
        self.fonte_entry = Font(family="Arial", size=12)
        self.fonte_botao = Font(family="Arial", size=12, weight="bold")

        self.lbl_titulo = Label(self.root, text="Sistema de Login", font=self.fonte_titulo, bg="#f0f0f0", fg="#4682b4")  
        self.lbl_titulo.pack(pady=(20, 10))  

        self.lbl_usuario = Label(self.root, text="Usuário:", font=self.fonte_label, bg="#f0f0f0")
        self.lbl_usuario.pack(pady=5)
        self.entry_usuario = Entry(self.root, font=self.fonte_entry)
        self.entry_usuario.pack(pady=5, padx=20, ipadx=50)

        self.lbl_senha = Label(self.root, text="Senha:", font=self.fonte_label, bg="#f0f0f0")
        self.lbl_senha.pack(pady=5)
        self.entry_senha = Entry(self.root, show="*", font=self.fonte_entry)
        self.entry_senha.pack(pady=5, padx=20, ipadx=50)

        self.btn_login = Button(self.root, text="Login", command=self.login, font=self.fonte_botao, bg="#4682b4", fg="white")
        self.btn_login.pack(pady=20, ipadx=10)

    def login(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()

        if usuario == "adm" and senha == "123":
            self.tipo_usuario = "Administrador"
        elif usuario == "maq" and senha == "123":
            self.tipo_usuario = "Maqueiro"
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
            return

        self.root.withdraw()
        TelaPrincipal(self.root, self.tipo_usuario).mostrar()

if __name__ == "__main__":
    root = Tk()
    Sistema(root)
    root.mainloop()
