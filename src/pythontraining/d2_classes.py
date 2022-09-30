import datetime as dt

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def say_hello(self):
        print(f"{self.name} says hello")

    def age(self):
        return (dt.datetime.today() - dt.datetime.strptime(self.birth_date, '%Y-%m-%d'))/365


p1 = Person("John", 42)
print(p1.name)
print(p1.age)

p2 = Person("Jane", 42)
p2.say_hello()


class Student(Person):

    def learn(self, language):
        print(f"{self.name} is learning {language}")

s1 = Student('John', 42)
s1.say_hello()
s1.learn('Java')

p1 = Person("John", "1978-01-01")
print(p1.name)
print(p1.age())