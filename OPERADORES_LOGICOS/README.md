# OPERADORES LOGICOS
Los operadores lógicos o logical operators nos permiten trabajar con valores de tipo booleano. Un valor booleano o bool es un tipo que solo puede tomar valores `True` o `False`.
# Operador and
El operador and evalúa si el valor a la izquierda y el de la derecha son `True`, y en el caso de ser cierto, devuelve `True`. Si uno de los dos valores es `False`, el resultado será `False`. 
> ejemplo
```python
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False
```
# Operador or
El operador or devuelve True cuando al menos uno de los elementos es igual a True. Es decir, evalúa si el valor a la izquierda o el de la derecha son True.
> ejemplo
```python
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False
```
# Operador not
Y por último tenemos el operador not, que simplemente invierte True por False y False por True. También puedes usar varios not juntos y simplemente se irán aplicando uno tras otro.
> ejemplo
```python
print(not True)  # False
print(not False) # True
print(not not not not True) # True
```
