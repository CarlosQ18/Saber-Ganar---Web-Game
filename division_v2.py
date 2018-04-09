def division_v1(a,b):
  c=a/b
  print("La division entre", a,"y",b, "es igual a", c)

def division_v2():
  bandera1=True
  bandera2=True
  while bandera1:
    try:
      a=int(input("Digite el numerador"))
    except ValueError:
      print("Digite nuevamente lel numerador")
    else:
      bandera1=False
  while bandera2:
    try:
      b=int(input("Digite el denominador"))
    except Exception:
      print("Digite nuevamente el denominador")
    else:
      if b==0:
        bandera2=True
        print("El resultado de la division por cero es indeterminado. Por favor ingrese nuevamente otro número diferente al cero")
      else:
        bandera2=False
        division_v1(a,b)
      
division_v2()
