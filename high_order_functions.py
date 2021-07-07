"""HIGH ORDER FUNCTION

Una función que recibe como parámetro otra función.
"""
    
def saludo(func):
    func()
    
def hola():
    print('Hola!')

def adios():
    print('Adios!')

saludo(hola)
saludo(adios)

""""""

# FILTER
my_list = [1,2,3,4,5,6,7,8,9,10]

# Usango lambda function y high order function
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)

# MAP
my_list = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x: x**2, my_list))
print(squares)

# REDUCE
my_list = [2, 2, 2, 2]

from functools import reduce
# Es necesario importar functools

# Se utiliza el primer elemento de la lista
# y el siguiente elemento
reduced = reduce(lambda a, b: a * b, my_list)


