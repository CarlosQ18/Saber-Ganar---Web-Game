import os
file_path=os.path.abspath(os.getcwd()) + '/logic/estado_juego.txt'
def estado_juego(correo):
  file=open(file_path,"a")
  vidas=5
  aciertos=0
  tabla=str(correo)+","+str(vidas)+","+str(aciertos)
  file.write(tabla)
  file.write("\n")


  
