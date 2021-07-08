class student:
    def __init__(self):
        self.name="kavin kumar R"
        self.parent="ramesh.S"
        self.teacher="tamil arasi"
        self.subject="python programming"
        print(self.name)
class parent(student):
    def __init__(self):
        print(self.parent)
        self.parent_opinion = 100
 class teacher(student,parent):
     def __init__(self):
         print(self.teacher)
         print(self.parent_opinion)
a=student()
a=parent()
a=teacher()