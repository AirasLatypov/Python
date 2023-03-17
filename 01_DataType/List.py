# customer = True
# # print(dir(customer))
# data = dir(customer)
# print(data)
# method = []
# for element in data:
#
#     if element[0:2] != '__':
#         method.append(element)
# print(method)
#
# my_list = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# my_dict = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# my_int = ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# my_str = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# my_float = ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
# my_bool = ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
#
#
# Append
'''
customer =[]
customer.append("Frank Sinatra")
customer.append(1915)
customer.append(1.72)
'''


# Создать рандомный список
'''
import random
numbers = []
while len(numbers) < 10:
    # print(f"Dlina List: {len(numbers)}, True/False: {len(numbers)} <= 10 Soderjimoy: {numbers}")
    value = random.randrange(start=1, stop=570)
    numbers.append(value)
    print(numbers)



my_list = []

while True:
    value = random.randrange(start=-20, stop=80)
    if value <= 10:
        print(f"KAPKAN Srabotal: {value}")
        break
    my_list.append(value)

# print(my_list)
'''


# CLEAR
'''methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
methods.clear()
print(methods)'''

# Copy
'''cars = ["BMW", "Nissan", "Ford", "Renault"]
transport = cars
automobile = cars.copy()
print(cars, transport, automobile, sep='\n')

print(cars == transport)
print(cars == automobile)

print(cars is transport)
print(cars is automobile)

print(f"{id(cars)} -- ID of 'cars'")
print(f"{id(transport)} -- ID of 'transport'")
print(f"{id(automobile)} -- ID of 'automobile'")'''

# Count
'''students = ['Edward', 'Katrine', 'Edward', 'Muriel', 'Katrine', 'Edward', 'Beverly']
print(students.count('Edward'))     # 3
print(students.count('Jordan'))     # 0
print(students.count('Katrine'))    # 2'''

# Extend
'''japan = ['Lexus', 'Acura', 'Infiniti', 'Toyota']
american = ['GMC', 'Chrysler', 'Dodge', 'Jeep']
automobile = []
automobile.extend(japan)
automobile.extend(american)
automobile.append(japan)
automobile.append(american)

print(automobile)'''

# INDEX
'''numbers = ['zero', 'one', 'two', 'three', 'one', 'five', 'six', 'one', 'one']
print(numbers.index('one'))         # 1
print(numbers.index('one', 0, 9))   # 1
print(numbers.index('one', 2, 9))   # 4
print(numbers.index('one', 5, 9))   # 7'''

# INSERT
''''data = [0, 1, 2, 3, 4, 5]
data.insert(0, "Info")      # ['Info', 0, 1, 2, 3, 4, 5]
data.insert(4, "Name")      # ['Info', 0, 1, 2, 'Name', 3, 4, 5]''''

# POP
'''cars = ["BMW", "Nissan", "Ford", "Renault", "Rusty Bucket"]
cars.pop()
print(cars)     # ['BMW', 'Nissan', 'Ford', 'Renault']
cars = ["BMW", "Nissan", "Ford", "Renault"]
cars.pop(0)
print(cars)     # ['Nissan', 'Ford', 'Renault']
cars = ["BMW", "Nissan", "Ford", "Renault"]
deleted_element = cars.pop(2)
print(deleted_element)          # Ford
print(cars)                     # ['BMW', 'Nissan', 'Renault']'''

# REMOVE
'''cars = ["BMW", "Nissan", "Ford", "BMW", "Renault"]
cars.remove("BMW")
print(cars)         # ['Nissan', 'Ford', 'BMW', 'Renault']'''

# REVERSE
'''data = [1, 'A', 'B', 4, 'E', 'F', 7]
data.reverse()
print(data)     # [7, 'F', 'E', 4, 'B', 'A', 1]'''

# SORT
'''data = [9, 2, 9, 7, 6, 2, 2, 3, 2]
data.sort()
print(data)     # [2, 2, 2, 2, 3, 6, 7, 9, 9]
data = [9, 2, 9, 7, 6, 2, 2, 3, 2]
data.sort(reverse=True)
print(data)     # [9, 9, 7, 6, 3, 2, 2, 2, 2]'''
