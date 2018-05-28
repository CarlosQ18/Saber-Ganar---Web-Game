import os
file_path=os.path.abspath(os.getcwd()) + '/logic/login.txt'
def getUsers():
	file=open(file_path,"r")
	userList=[]
	lineas=file.readlines()
	for linea in lineas :
		linea_nueva=linea.replace("\n","")
		lista=linea_nueva.split(",")
		userList.append(lista)
	return userList
	file.close()

def userExist (username,userList):
        
	exist=[]
	for user in userList:
		if username in user:
			exist=user
			break
	return exist


def checkPassword(user,password):
	return True if password in user else False

def ingreso(username,password):
	userList=getUsers()
	user=userExist(username,userList)
	if len(user)>0:
		if checkPassword(user,password):
			return True
		else:
			return False
	else:
		return False
