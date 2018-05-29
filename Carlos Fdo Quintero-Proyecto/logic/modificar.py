import os
filepath=os.path.abspath(os.getcwd()) + '/logic/datos_estudiantes.txt'
filepath2=os.path.abspath(os.getcwd()) + '/logic/estado_juego.txt'

def modificar_grado(correo,grado):
  f = open(filepath,"r")
 
# Creamos una lista con cada una de sus lineas
  lineas = f.readlines()
 
# abrimos el archivo pero vacio
  f = open(filepath,"w")
 
# recorremos todas las lineas para modificar el grado
  for linea in lineas:
    linea=linea.replace("\n"," ")
    sub_list=linea.split(",")
    if correo in sub_list:
      sub_list[4]=str(grado)
      linea= ','.join(sub_list)+"\n"
      f.write(linea)
    else:
      linea= ','.join(sub_list)+"\n"
      f.write(linea)
  f.close()
def modificar_vidas(correo,vidas,aciertos):
  f = open(filepath2,"r")
 
# Creamos una lista con cada una de sus lineas
  lineas = f.readlines()
 
# abrimos el archivo pero vacio
  f = open(filepath2,"w")
 
# recorremos todas las lineas para modificar las vidas y aciertos
  for linea in lineas:
    linea=linea.replace("\n"," ")
    sub_list=linea.split(",")
    if correo in sub_list:
      sub_list[1]=str(vidas)
      sub_list[2]=str(aciertos)
      linea= ','.join(sub_list)+"\n"
      f.write(linea)
    else:
      linea= ','.join(sub_list)+"\n"
      f.write(linea)
  f.close()
