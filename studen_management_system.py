class Student:
    def __init__(self,r,n,f,m):
        self.r,self.n,self.f,self.m=r,n,f,m
    def show(self):
        print(self.r,self.n,self.f,self.m)

class Database:
    def __init__(self):
        self.d=[]
    def add(self,s):
        if not any(x.r==s.r for x in self.d): self.d.append(s)
    def remove(self,r):
        self.d=[x for x in self.d if x.r!=r]
    def view(self):
        for x in self.d: x.show()
        print("Total:",len(self.d))

db=Database()

while True:
    print("\n1.Add 2.Remove 3.View 4.Update 5.Exit")
    c=input("Choice: ")

    if c=="1":
        db.add(Student(int(input("Roll: ")),input("Name: "),
                       input("Father: "),input("Mobile: ")))

    elif c=="2":
        db.remove(int(input("Roll: ")))

    elif c=="3":
        db.view()

    elif c=="4":
        r=int(input("Roll: "))
        for x in db.d:
            if x.r==r:
                x.n=input("Name: ")
                x.f=input("Father: ")
                x.m=input("Mobile: ")

    elif c=="5":
        break
