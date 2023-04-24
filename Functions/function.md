# Functions 

## Example
---
```python
def sayHello():                 # Задаем функцию.
    print("Hello")              # Наполняем функцию.
    print("World")
    print("Super")

sayHello()                      # Запускаем функцию.(Распечатает все 3 принта)
```
---
```python
def square(x):                                      # Задаем функцию.
    print("Квадрат числа" , x, "=", x ** 2)         # Наполняем функцию.

square(5)                                           # Квадрат числа 5 = 25. Вместо 5 любое число.
```
---
```python
def multiplay(a, b):                    # Задаем функцию.
    print(a*b)                          # Наполняем функцию.

multiplay(3, 5)                         # Ответ 5. a и b любые числа.
```
---
```python
def repeat_please_n_times(n):           # Задаем функцию.
    for i in range(n):                  # Наполняем функцию. n раз вывести слова "Just do it"
        print("Just do it")
repeat_please_n_times(3)                # Задаем колличество 3. Можно любое.
```
---
