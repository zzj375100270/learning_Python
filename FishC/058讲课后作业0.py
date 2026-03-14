class Person:
    name = ""
    age = 0
    def set_name(self):
        self.name = input("请输入姓名：")
        print(f"已将姓名设置为'{self.name}'")
    def set_age(self):
        self.age = int(input("请输入年龄："))
        print(f"已将年龄设置为'{self.age}'")
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
p = Person()
p.set_name()
p.set_age()
print(f"姓名：{p.get_name()}")
print(f"年龄：{p.get_age()}")