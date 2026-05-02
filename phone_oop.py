class phone():
    def __init__(self,colour,brand,passcode,age,price):
        self.colour=colour
        self.brand=brand

        self.passcode=passcode
        self.age=age
        self.price=price

    def showDetails(self):

        print(self.colour)
        print(self.brand)
        print(self.passcode)

        print(self.age)
        print(self.price)

    def unlock(self):
        code=input("enter passcode: ")

        if code==self.passcode:
            print("phone unlocked")
        else:
            print("wrong passcode")


    def update_all(self):

        self.colour=input("enter new colour: ")
        self.brand=input("enter new brand: ")

        self.passcode=input("enter new passcode: ")
        self.age=input("enter phone age: ")

        self.price=input("enter new price: ")


p1=phone("black","apple","1234",2,"£500")


p1.showDetails()

p1.update_all()

p1.showDetails()


p1.unlock()