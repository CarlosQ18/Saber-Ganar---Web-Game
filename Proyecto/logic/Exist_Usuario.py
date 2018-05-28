import os
file_path=os.path.abspath(os.getcwd()) + '/logic/login.txt'
def getUsers():
	file=open(file_path,"r")
	userList=[]
	lineas=file.readlines()
	for linea in lineas :
		linea_nueva=linea.replace("\n","")
		lista=linea_nueva.split(",")
		userList.append(lista[0])
	return userList
	file.close()

getUsers()
def repetido(username):
        userList=getUsers()
        if username in userList:
                return True
        else:
                return False