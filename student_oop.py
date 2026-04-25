class student():
    def __init__(self,age,grade,year,name,username,password):
        self.age=age
        self.grade=grade
        self.year=year
        self.name=name
        self.username=username
        self.password=password



    def showDetails(self):
        print(self.age)
        print(self.year)
        print(self.grade)
        print(self.name)
        
    
    def login(self):
        user=input("What is your usename: ")
        if user == self.username:
            pass_w=input("What is your password: ")
            if pass_w==self.password:
                print("Access Granted")
            else:
                print("Password is not correct ")

        else:
            print("Access Not Granted")



    def update_grade(self):
        grade_1=input("What is the new grade? ")
        self.grade=grade_1




o1=student(12,"A",8,"John,","John_123","Hello_5")
o2=student(15,"B",10,"Emily","Emily_123", "Hi_5" )

o1.showDetails()
o1.update_grade()
o1.showDetails()
o1.login()

# o2.login()

