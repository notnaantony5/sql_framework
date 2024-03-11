lst = [1, 2, 3, 4, 5]
gen = ({
    i: i * i
    for i in lst
    if not i % 2})
names = ['John', 'Smith', 'Alice', 'Victor', 'David']
dct = {name: len(name)
       for name in names
       if 'a' not in name.lower()
       and 'r' not in name.lower()}
"""
Нужно собрать при помощи словарного включения словарь
В котором ключ - имя, значение - количество символов 
в имени при условии что берем имена в которых нет букв
'A' и 'R' в обоих регистрах { 'John': 4, 'Smith': 5 }
"""
personal = [
    {'name': 'John', 'age': 20, 'salary': 1000},
    {'name': 'Smith', 'age': 30, 'salary': 1700},
    {'name': 'Alice', 'age': 35, 'salary': 7000},
    {'name': 'Victor', 'age': 26, 'salary': 2100}
]
"""Метрика: зарплата разделенная на количество лет 
после совершеннолетия. 1000 / (20 - 18) = 500
1700 / (30 - 18) = 141
Нужно собрать только имена людей в список, где 
эта метрика будет >= 300
"""