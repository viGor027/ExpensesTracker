from database import DataBase as Db
from .dashboard import Dashboard as Dash
import customtkinter

class Login:
    def __init__(self, database: Db, register):
        self.db = database
        self.reg = register
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login")
        self.u_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.u_pwd_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.__login_acces)
        self.button_reg = customtkinter.CTkButton(master=self.frame, text="Register", command=self.__login_register)

        self.label_prompt = customtkinter.CTkLabel(master=self.frame, text="Nieprawidłowe hasło")
        self.label_prompt2 = customtkinter.CTkLabel(master=self.frame, text="Nie ma takiego użytkownika, \n sprawdź dane, lub zarejestruj się")


    def login_view(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.label.pack(pady=12, padx=10)
  
        self.u_name_entry.pack(pady=12, padx=10)
  
        self.u_pwd_entry.pack(pady=12, padx=10)
  
        self.button.pack(pady=12, padx=10)
        self.button_reg.pack(pady=2, padx=10)

        self.root.mainloop()


    def __login_acces(self):
        self.label_prompt.pack_forget()
        self.label_prompt2.pack_forget()

        exists = self.db.user_exists(self.u_name_entry.get())

        if exists:
            q2 = "SELECT * FROM Login"
            for result in self.db.query(q2):
                username = result[0]
                password = result[1]

            if password == self.u_pwd_entry.get():
                self.root.destroy()
                d = Dash(self.db) # tutaj podać mu username,
                d.dashboard_view() # żeby mógł szukać w bazie rzeczy związanych z tym użytkownikiem
            else:
                self.label_prompt.pack(pady=5)
            
        else:
            self.label_prompt2.pack(pady=5)

    def __login_register(self):
        self.root.destroy()
        self.reg.register_view()
        