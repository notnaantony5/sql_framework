from framework import Model, String, Integer, run


class Person(Model):
    name: String
    age: Integer


class Salary(Model):
    salary: Integer
    person: Integer


# run()
# Person.create(name='John', age=4)

persons = [{
    'name': 'John',
    'age': 14
},
    {
        'name': 'Andrew',
        'age': 22
    }]


class AgeFilter:
    def __init__(self, start_age=0, end_age=None, key=None):
        self.key = key
        self.start_age = start_age
        self.end_age = end_age

    def __call__(self, age: int) -> bool:
        if self.key is not None:
            age = self.key(age)
        if age < self.start_age:
            return False
        if self.end_age is not None:
            if age > self.end_age:
                return False
        return True


print(list(
    filter(AgeFilter(start_age=18, key=lambda x: x['age']), persons)
))
print(list(
    filter(AgeFilter(end_age=18, key=lambda x: x['age']), persons)
))

class NameFilter:
    def __init__(self, letter):
        self.letter = letter.lower()



    def __call__(self, name: str) -> bool:
        return self.letter in name.lower()

names = ['Антон', 'Евгений', 'Алиса']

print(
    list(
        filter(NameFilter('лиса'), names)
    )
)

class Human:
    def __init__(self, name):
        self.name = name
        self.зззз = 4

    def __call__(self):
        print(self.name)

h1 = Human('Саша')
h2 = Human('Егор')
h1()
h2()

print(h1.зззз)