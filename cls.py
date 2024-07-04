# class is a collection of no of functions

class marksheet:
    def bi(self,roll,nm):
        self.rollno=roll
        self.name=nm
    def marks(self,s1,s2,s3):
        self.total=s1+s2+s3
        self.per=self.total/3
    def result(self):
        print("Rollno=",self.rollno)
        print("Name=",self.name)
        print("Total=",self.total)
        print("per=",self.per)
        if(self.per>50):
            print("Pass")
        else:
            print("Fail")        

ob=marksheet()
ob.bi(101,"xyz")
ob.marks(89,78,88)
ob.result()            