class User:
    def __init__(self, uname: str, pwd: str, exps: list, inc: list) -> None:
        self.username = uname
        self.password = pwd
        self.expenses = exps
        self.income = inc

    def __repr__(self) -> str:
        return f'Username: {self.username}, Expenses: {self.expenses}, Income: {self.income}'