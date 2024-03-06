from framework import Model, String, Integer, run

class Person(Model):
    name: String
    age: Integer

class Salary(Model):
    salary: Integer
    person: Integer

run()