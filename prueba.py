from datetime import datetime

import openpyxl

openpyxl.open

"""
my_dict = {
    'nombre': "Pedro",
    'apellido': "Busato",
    'edad': 22
}

my_tuple = ('Pedro', 'Busato', 22, [1,2,3])
print([1,2,3] in my_tuple) # True

print(my_tuple.index(22))




my_list = ['Pedro', 'Busato', 22, [1,2,3]]
print(my_list.index(22))

print(my_dict['apellido'])

alumnos = ['juan', 'alejo', 'pedro']
enumerateAlumnos = enumerate(alumnos)
print(list(enumerateAlumnos))               # [(0, 'juan'), (1, 'alejo'), (2, 'pedro')]


current_date = datetime.now()
print(current_date)                         # 2023-09-10 10:05:34.458122
print(current_date.day)                     # 10
print(current_date.month)                   # 9
print(current_date.year)                    # 2023



#strftime --> Convert date format to string format
current_date = datetime.now()
print(type(current_date))                               # <class 'datetime.datetime'>
current_date_string = current_date.strftime("%d/%m/%y")
print(current_date_string)                              # 10/09/2023
print(type(current_date_string))                        # <class 'str'>


#strptime --> Convert string format to date format
current_date_string = '2022-12-31'
print(type(current_date_string))                                    # <class 'str'>
current_date = datetime.strptime(current_date_string, "%Y-%m-%d")
print(current_date)                                                 # 2022/12/31
print(type(current_date))                                           # <class 'datetime.datetime'>
"""