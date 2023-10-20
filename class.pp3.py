class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width


    def area(self):
        print(self.length*self.width)




cls_shp=Shape
cls_rct=Rectangle
length=int(input())
width=int(input())
cls_rct.area(cls_rct(length,width))