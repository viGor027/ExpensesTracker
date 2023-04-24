from database import DataBase as Db
import customtkinter
import tkinter

class Dashboard:
    def __init__(self,  database: Db, user: str):
        self.db = database
        self.user = "Użytkownik: " + user
        
        self.root = customtkinter.CTk()
        self.root.geometry("700x500")

        self.frame_left = customtkinter.CTkFrame(master=self.root,
                                                 width=200,
                                                 height=400,
                                                 corner_radius=10)
        self.frame_left.pack(pady=12, padx=10, anchor=tkinter.E)


        self.frame_right = customtkinter.CTkFrame(master=self.root,
                                                  width=420,
                                                  height=400,
                                                  corner_radius=10)
        self.frame_right.pack(pady=12, padx=10, anchor=tkinter.W)


        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                                text=self.user,
                                                width=30,
                                                height=20,
                                                fg_color=("white", "gray38"),
                                                corner_radius=8)
        self.label_1.pack(pady=12, padx=10, anchor=tkinter.CENTER)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                                text="Bilans: ",
                                                width=30,
                                                height=20,
                                                fg_color=("white", "gray38"),
                                                corner_radius=8)
        self.label_2.pack(pady=12, padx=10, anchor=tkinter.CENTER)

        self.expense_in = customtkinter.CTkEntry(master=self.frame_right, placeholder_text="Wprowadź wydatek")
        self.expense_in.pack(pady=12, padx=10, anchor=tkinter.CENTER)
        self.button_expense_in = customtkinter.CTkButton(master=self.frame_right, text="Zatwierdź", command=self.__button_expense_in)
        self.button_expense_in.pack(pady=12, padx=10, anchor=tkinter.CENTER)

    def dashboard_view(self):
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())
        self.root.mainloop()

    def __button_expense_in(self):
        print("przycisk")