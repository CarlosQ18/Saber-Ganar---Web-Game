import os
filepath=os.path.abspath(os.getcwd()) + '/logic/preguntastomadas.txt'
def pregunta_vista(id_pregunta,correo,grado):
  file=open(filepath,"a")
  tabla=str(id_pregunta)+","+str(correo)+","+str(grado)
  file.write(tabla)
  file.write("\n")
  
