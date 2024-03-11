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
