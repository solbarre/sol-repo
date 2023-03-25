nombres = 10

a = 0
b = 1
total = 0

print("Les 10 premiers nombres de la suite de Fibonacci sont :".format(nombres), end = " ")
for _ in range(nombres):
  print(total, end = " ")
  a = b
  b = total
  total = a + b