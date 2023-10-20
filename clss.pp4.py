import math

class point:
    def __init__(self, a = 7  , b = 2 ):
        self.a  = a
        self.point_b  = b

    def show(self):
        print(f'{self.point_a}'+ ' '+ f'{self.point_b}')

    def move(self, a , b):
        self.a = a
        self.b = b
        print('Changed coordinates:',self.a,self.b)

    def dist(self,a,b):
        d = math.sqrt(pow((self.a - a),2) + pow((self.b - b),2))
        print(d)

p = point()
p.show()

p.move(7 , 8)
second_point = point(1 , 1)

second_point.show()
p.show()

p.dist(5,9) 