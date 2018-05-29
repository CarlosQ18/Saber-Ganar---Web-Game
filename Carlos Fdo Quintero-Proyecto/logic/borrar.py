import os
filepath=os.path.abspath(os.getcwd()) + '/logic/preguntastomadas.txt'

def borrar(correo,grado):
  f = open(filepath,"r")
 
# Creamos una lista con cada una de sus lineas
  lineas = f.readlines()
# abrimos el archivo pero vacio
  f = open(filepath,"w")
 
# recorremos todas las lineas para borrar la pregunta que ya se ha visto en el grado,tras haber perdido año
  for linea in lineas:
    linea=linea.replace("\n"," ")
    sub_list=linea.split(",")
    
    if (correo in sub_list):
      print(sub_list)
      print(sub_list[2])
      if int(sub_list[2])==int(grado):
        pass
      else:
        linea= ','.join(sub_list)+"\n"
        f.write(linea)
        
    else:
      linea= ','.join(sub_list)+"\n"
      f.write(linea)
  f.close()
