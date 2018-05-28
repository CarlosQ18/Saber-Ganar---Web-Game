
from flask import Flask,flash,render_template,url_for,g
from flask import request
from flask import redirect
import os
from logic.ingreso import ingreso
from logic.Exist_Usuario import repetido
from logic.Datos_estudiantes import Datos_estudiantes
from logic.buscar import*
from logic.Estado_juego import estado_juego
from logic.diccionario import getCourseDiccionary
from logic.borrar import*
from logic.modificar import*
from logic.pregunta_vista import*
import json
app=Flask(__name__,static_folder='static')
correo=""
d=[]
@app.route('/')
def index():
        return render_template('Ingreso.html')

@app.route('/login',methods=['GET','POST'])
def login():
	global correo,d
	if request.method=='POST':
		correo=request.form ["correo"]
		password=request.form["password"]
		n=buscar_nombre(correo)
		gr=buscar_grado(correo)
		ac=buscar_aciertos(correo)
		v=buscar_vidas(correo)
		d=getCourseDiccionary(correo,gr)
		if ingreso(correo,password):
			return render_template('juego.html',nombre=n,grado=gr,aciertos=ac,vidas=v, dic=d)
		if correo=="admin" and password=="1234":
			return render_template('Registro.html')
		else:
			return redirect(url_for('index'))

@app.route('/registrar',methods=['GET','POST'])
def registrar():
	if request.method=='POST':
		nombre=request.form ["nombre"]
		correo=request.form["correo"]
		password=request.form["password"]
		codigo=request.form["codigo"]
		edad=request.form["edad"]
		grado=request.form["grado"]
		if not(nombre=="" or correo=="" or password=="" or codigo=="" or edad=="" or grado==""):
			if not repetido(nombre):
				Datos_estudiantes(nombre,correo,password,codigo,edad,grado)
				estado_juego(correo)
				return render_template('Registro.html')
			else:
				flash("El usurio ya existe","error")
				return render_template('Registro.html')
		else:
			print('LLene todos los campos')
			return render_template('Registro.html')
@app.route('/game', methods=['GET','POST'])
def game():
	print(correo)
	if request.method=='POST':
		opcion=request.form['opcion']
		id_pregunta=request.form['id_pregunta']
		vidas1=request.form['vid']
		aciertos=request.form['act']
		grade=request.form['grade']
		print(grade)
		graduar=request.form['graduarse']
		print(graduar)
		if graduar=="no":
			pregunta_vista(id_pregunta,correo,grade)
			modificar_vidas(correo,vidas1,aciertos)
		if graduar=="perder":
			modificar_vidas(correo,vidas1,aciertos)
			borrar(correo,grado)
		if graduar=="ganar":
			d=getCourseDiccionary(correo,grade)
			modificar_grado(correo,grade)
			modificar_vidas(correo,vidas1,aciertos)
			print(d)

		return ('', 204)
@app.route('/logout',methods=['GET','POST'])
def logout():
	return redirect(url_for('index'))
if __name__=='__main__':
  app.run(debug=True)
