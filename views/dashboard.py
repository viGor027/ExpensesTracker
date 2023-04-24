from database import DataBase as Db
# from .dashboard import Dashboard as Dash
# from .register import Register as Reg
import customtkinter

class Dashboard:
    def __init__(self,  database: Db):
        self.db = database
        print("dashboard initialized")

    def dashboard_view(self):
        print("dashboardview")