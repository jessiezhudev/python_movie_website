class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("last_name:" + self.last_name)
        print("eye_color:" + self.eye_color)
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
    def show_info(self):
        print("child_last_name:" + self.last_name)
xiongzhu = Parent("zhu", "brown")
jessiezhu = Child("zhu","blue","5")
jessiezhu.show_info()
# print(jessiezhu.eye_color)
