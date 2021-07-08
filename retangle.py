class Retangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Print_area(self):
        print("the area is ",self.length*self.breadth)
    def Print_perimeter(self):
        print("the perimeter is ",2*(self.length+self.breadth))
class square(Retangle):
    def __init__(self,side):
        super().__init__(side,side)


#OBJECT FOR RECTANGLE
rec=Retangle(10,5)
rec.Print_area()
rec.Print_perimeter()


#OBJECT FOR SQUARE
sq=square(5)
sq.Print_perimeter()
sq.Print_area()


