# viet chuong trinh de s dung tinh tru tượng trong python , truu tuong la co che cho phep chung ta tao ra cac lop va phuong thuc m akhong can cung cap cu the hanh vi hoac gia tri
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "gâu gâu"

class Cat(Animal):
    def sound(self):
        return "meo meo"

dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())