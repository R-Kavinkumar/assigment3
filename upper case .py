class demo :
    def __init__(self):
        self.str=""
    def get_string(self):
        self.str=input("enter the string to change it to upper case: ")
        return
    def print_string(self):
        self.str=self.str.upper()
        print(self.str)
obj=demo()
obj.get_string()
obj.print_string()
