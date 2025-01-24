class Student:
    name = ""
    age = 0
    clas = 0
    prefer_subject = ""
    def __init__(self, name="", age=0, clas=0, prefer_subject=""):
        self.name = name
        self.age = age
        self.clas = clas
        self.prefer_subject = prefer_subject


    def hello_teacher(self, teachers_name="учитель"):
        print(f"Здравствуйте,{teachers_name}!")

    def To_beat(self, beating_name="", beated_name=""):
        print(f"Ужас!{beating_name} побил {beated_name}")

stdnt = Student()
stdnt.hello_teacher("Степан")


