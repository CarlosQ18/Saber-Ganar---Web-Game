import os
file_path1=os.path.abspath(os.getcwd()) + '/logic/login.txt'
file_path2=os.path.abspath(os.getcwd()) + '/logic/datos_estudiantes.txt'
def Datos_estudiantes(nombre,correo,password,codigo,edad,grado):
  file2=open(file_path2,"a")
  tabla2=str(nombre)+","+str(correo)+","+str(codigo)+","+str(edad)+","+str(grado)
  file2.write(tabla2)
  file2.write("\n")
  file1=open(file_path1,"a")
  tabla1=str(correo)+","+str(password)
  file1.write(tabla1)
  file1.write("\n")
