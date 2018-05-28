import os
file_path=os.path.abspath(os.getcwd()) + '/logic/estado_juego.txt'
file_path2=os.path.abspath(os.getcwd()) + '/logic/datos_estudiantes.txt'

def buscar_vidas(correo):
  f=open(file_path,"r")
  f.readline()
  for line in f:
    line=line.replace("\n"," ")
    sub_list=line.split(",")
    if correo in sub_list:
      vidas=int(sub_list[1])
      return vidas

def buscar_aciertos(correo):
  f=open(file_path,"r")
  f.readline()
  for line in f:
    line=line.replace("\n"," ")
    sub_list=line.split(",")
    if correo in sub_list:
      aciertos=int(sub_list[2])
      return aciertos

def buscar_grado(correo):
  f=open(file_path2,"r")
  f.readline()
  for line in f:
    line=line.replace("\n"," ")
    sub_list=line.split(",")
    if correo in sub_list:
      grado=int(sub_list[4])
      return grado

def buscar_nombre(correo):
  f=open(file_path2,"r")
  f.readline()
  for line in f:
    line=line.replace("\n"," ")
    sub_list=line.split(",")
    if correo in sub_list:
      nombre=str(sub_list[0])
      return nombre
