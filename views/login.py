from database import DataBase as Db
from .dashboard import Dashboard as Dash
from .register import Register as Reg
import customtkinter

class Login:
    def __init__(self, database: Db):
        self.db = database
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login")
        self.u_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.u_pwd_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.__login_acces)

    def login_view(self, dashboard: Dash, register: Reg):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.label.pack(pady=12, padx=10)
  
        self.u_name_entry.pack(pady=12, padx=10)
  
        self.u_pwd_entry.pack(pady=12, padx=10)
  
        self.button.pack(pady=12, padx=10)

        self.root.mainloop()


    def __login_acces(self):
        # self.db.push("Expenses", [("test", "wydatek", 20)])
        # for i in self.db.pull_rows("Expenses"):
        #     print(i)
        print(self.u_name_entry.get())