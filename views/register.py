from database import DataBase as Db
from .login import Login as Login
import customtkinter

class Register:
    def __init__(self, database: Db):
        self.db = database

        self.root = customtkinter.CTk()
        self.root.geometry("500x350")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Rejestracja")
        self.u_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.u_pwd_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.u_confirm_pwd_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text=" Confirm password", show="*")

        self.button_reg = customtkinter.CTkButton(master=self.frame, text="Zarejestruj się", command=self.__register_register)
        self.button_back = customtkinter.CTkButton(master=self.frame, text="Wróć do logowania", command=self.__back_to_login)

        self.label_prompt = customtkinter.CTkLabel(master=self.frame, text="Taki użytkownik już istnieje, \n zaloguj się, lub wybierz inną nazwe użytkownika")
        self.label_prompt2 = customtkinter.CTkLabel(master=self.frame, text="Podane hasła nie są takie same, \n spróbuj jeszcze raz")
        self.label_prompt3 = customtkinter.CTkLabel(master=self.frame, text="Pomyślnie zarejestrowano, \n możesz się zalogować :)")
        self.label_prompt4 = customtkinter.CTkLabel(master=self.frame, text="Pola nie mogą być puste!")
    def register_view(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.label.pack(pady=12, padx=10)
  
        self.u_name_entry.pack(pady=5, padx=10)
  
        self.u_pwd_entry.pack(pady=5, padx=10)
        self.u_confirm_pwd_entry.pack(pady=5, padx=10)

        self.button_reg.pack(pady=2, padx=10)
        self.button_back.pack(pady=12, padx=10)
        

        self.root.mainloop()
    
    def __register_register(self):
        self.label_prompt.pack_forget()
        self.label_prompt2.pack_forget()
        self.label_prompt3.pack_forget()
        self.label_prompt4.pack_forget()

        username = self.u_name_entry.get()

        exists = self.db.user_exists(username)
        pwd = self.u_pwd_entry.get()
        confirm_pwd = self.u_confirm_pwd_entry.get()

        if len(username) == 0 or len(pwd) == 0 or len(confirm_pwd) == 0:
            self.label_prompt4.pack()
        elif exists:
            self.label_prompt.pack()
        elif pwd != confirm_pwd:
            self.label_prompt2.pack()
        else:
            self.db.push("Login", [(username, pwd)])
            self.label_prompt3.pack()

    def __back_to_login(self):
        self.root.destroy()
        n_reg = Register(self.db)
        lg = Login(self.db, n_reg)
        lg.login_view()