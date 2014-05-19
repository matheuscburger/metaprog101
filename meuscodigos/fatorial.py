def fatorial(n):
  """devolve n!"""
  return 1 if n < 2 else n*fatorial(n-1)

type(fatorial)	# fatorial eh um objeto da classe function
fat = fatorial
fat(10)

map(fat, range(1,10))	# devolve um gerador
list(map(fat, range(1,10)))

[fat(n) for n in range(1,10)]	# usando list comprehension

dir()	# namespace global


x = "Garoa"
dir(x)

# __ add__ 
x + "!!!"


#x+1 # erro

# __doc__
x.__doc__
help(str)

dir(fatorial)

help(fatorial)

# __call__
fatorial.__call__(5)

# posso criar um objeto que se comporta como uma funcao
# basta criar o método __call__

# _ armazena o resultado da ultima chamada no console
# porem não funciona em scripts

# Inspeção em tempo de execucao
#>>> _
#<code object fatorial at 0x7f03dd402ad0, file "<string>", line 1>
#>>> dir(_)
#['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
#>>> fat.__code__
#<code object fatorial at 0x7f03dd402ad0, file "<string>", line 1>
#>>> fat.__code__.co_names
#('fatorial',)
#>>> fat.__code__.co_varnames
#('n',)


import dis	# disassembly

dis.dis(fat.__code__.co_code)
