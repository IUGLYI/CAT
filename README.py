# CAT

class Cat():
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def description_name(self):
        desc = self.name + ' ' + self.gender + ' ' + str(self.age) + ' ' + self.breed
        return desc.title()


cat1 = Cat('Baron', 'Boy', 2, 'Siberian')
cat2 = Cat('Sam', 'Boy', 2, 'Siberian')

print(cat1.description_name())
print(cat2.description_name())
