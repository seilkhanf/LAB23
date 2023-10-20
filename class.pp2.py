class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length=length


    def area(self):
        print(self.length**2)




cls_shp=Shape
cls_sqr=Square
length=int(input())
cls_sqr.area(cls_sqr(length))