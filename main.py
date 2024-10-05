# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


               #module_6_1
class Animal:   #животное
    alive = True  # живой
    fed = False   # накормлен
    def __init__(self, name):
        self.name = name
    def eat(self, food):
            if isinstance(food, Plant):
                if food.edible:
                    print(f"{self.name} съел {food.name}")
                    self.fed = True
                else:
                    print(f"{self.name} не стал есть {food.name}")
                    self.alive = False
            

class Plant: # растение
    edible = False # съедобность
    def __init__(self, name):
        self.name = name
class Mammal(Animal):# млекопитающие
    pass
class Predator(Animal):# животные
    pass
class Flower(Plant): # цветок
    pass
class Fruit(Plant): # фрукт
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('лев')
a2 = Mammal('заяц')
p1 = Flower('борщевик')
p2 = Fruit('яблоко')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
