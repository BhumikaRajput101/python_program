#Area and Perimeter of shapes

class shape():
    def area(self, length , wigdth):
        self.length=length
        self.wigdth=wigdth
        return self.length*self.wigdth
class square(shape):
    def area(self,length, wigdth):
        self.length=length
        self.wigdth=wigdth
        return self.length*self.wigdth
class circle(shape):
        def area(self,radius):
            self.radius=radius
            return 3.14*self.radius * self.radius
shape1=square()
shape2=circle()
print(shape1.area(2,4))
print(shape2.area(2))