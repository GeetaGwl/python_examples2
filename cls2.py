class calc:
    def input(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        z=self.x+self.y
        print("sum is",z)    
    def multiply(self):
        z=self.x*self.y
        print("ans is",z)    


c=calc()  
c.input(10,2)
c.sum()
c.multiply()      