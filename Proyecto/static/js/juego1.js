var coorx=6
	var coory=1
	document.addEventListener('keydown',function(event){
		if (nivel==1){

			var map1=[
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
					[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
					[1,0,1,2,1,0,1,3,1,0,1,4,1,0,1,5,1,0,1],
					[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
					[1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1],
					[1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1],
					[1,0,1,1,6,1,1,0,0,0,0,1,1,7,1,1,0,0,1],
					[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			]
		
			if (event.keyCode==37 && map1[coorx][coory-1]!=1){
				moverizq();
				coory-=1
				
			}
			
			if (event.keyCode==38 && map1[coorx-1][coory]!=1){
				moverarriba();
				coorx-=1
				if (map1[coorx][coory]==2){
					console.log('Grado Kinder')
				}
				if (map1[coorx][coory]==3){
					console.log('Grado 1')
				}
				if (map1[coorx][coory]==4){
					console.log('Grado 2')
				}
				if (map1[coorx][coory]==5){
					console.log('Grado 3')
				}
				if (map1[coorx][coory]==6){
					console.log('Grado 4')
				}
				if (map1[coorx][coory]==7){
					console.log('Grado 5')
				}
			}
			if (event.keyCode==39  && map1[coorx][coory+1]!=1){
				moverder();
				coory+=1
				if (map1[coorx][coory]==9){
					console.log('Nivel 2')
					nivel+=1
					coorx=6
					coory=1
					posx=0
					posy=195
				}

			}
			if (event.keyCode==40  && map1[coorx+1][coory]!=1){
				moverabajo();
				coorx+=1
			}
		}
		if (nivel==2){

			var map1=[
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],
					[1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],
					[8,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,9],
					[8,0,1,1,2,1,1,0,1,1,1,0,1,3,1,1,1,0,9],
					[8,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,9],
					[8,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,9],
					[8,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,9],
					[1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
					[1,1,1,4,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
					[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			]
		
			if (event.keyCode==37 && map1[coorx][coory-1]!=1){
				moverizq();
				coory-=1
				if (map1[coorx][coory]==8){
					console.log('Nivel 1')
					nivel-=1
					coorx=6
					coory=18
					posx=544
					posy=195

				}
				
			}
			
			if (event.keyCode==38 && map1[coorx-1][coory]!=1){
				moverarriba();
				coorx-=1
				if (map1[coorx][coory]==2){
					console.log('Grado 6')
				}
				if (map1[coorx][coory]==3){
					console.log('Grado 7')
				}
				if (map1[coorx][coory]==4){
					console.log('Grado 8')
				}
			}
			if (event.keyCode==39  && map1[coorx][coory+1]!=1){
				moverder();
				coory+=1
				if (map1[coorx][coory]==9){
					console.log('Nivel 3')
					nivel+=1
					coorx=6
					coory=1
					posx=0
					posy=195
				}

			}
			if (event.keyCode==40  && map1[coorx+1][coory]!=1){
				moverabajo();
				coorx+=1
			}
		}
			if (nivel==3){

			var map1=[
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
					[1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],
					[1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],
					[8,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1],
					[8,0,1,1,2,1,1,0,1,1,1,0,1,3,1,1,1,0,1],
					[8,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
					[8,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
					[8,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
					[1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
					[1,1,1,4,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
					[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
					[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
			]
		
			if (event.keyCode==37 && map1[coorx][coory-1]!=1){
				moverizq();
				coory-=1
				if (map1[coorx][coory]==8){
					console.log('Nivel 2')
					nivel-=1
					coorx=6
					coory=18
					posx=544
					posy=195

				}
				
			}
			
			if (event.keyCode==38 && map1[coorx-1][coory]!=1){
				moverarriba();
				coorx-=1
				if (map1[coorx][coory]==2){
					console.log('Grado 9')
				}
				if (map1[coorx][coory]==3){
					console.log('Grado 10')
				}
				if (map1[coorx][coory]==4){
					console.log('Grado 11')
				}
			}
			if (event.keyCode==39  && map1[coorx][coory+1]!=1){
				moverder();
				coory+=1

			}
			if (event.keyCode==40  && map1[coorx+1][coory]!=1){
				moverabajo();
				coorx+=1
			}
		}
	})


	var imgder,imgesp,imgfrente,imgizq
	function cargaImagenes(){
		imgmap=new Image();
		imgmap2=new Image();
		imgder=new Image();

		imgmap.src='../static/img/mapa.png';
		imgmap2.src='../static/img/mapa2.png';
		imgder.src='../static/img/der.png';

	}
	function dibujamapa(){
		ctx.drawImage(imgmap,0,0,544,416,0,0,544,416);
	}
	function dibujamapa2(){
		ctx.drawImage(imgmap2,0,0,544,416,0,0,544,416);
	}
	var nivel=1
	var posx=0
	var posy=195
	var pasos=32
	function dibujaDer(){
		ctx.drawImage(imgder,0,0,32,48,posx,posy,30,30);
	}
	function moverder(){
		posx+=pasos
	}
	function moverizq(){
		posx-=pasos
	}
	function moverarriba(){
		posy-=pasos
	}
	function moverabajo(){
		posy+=pasos

	}
	function identificar_nivel(nivel){
		if (nivel==1){
			dibujamapa();
		}
		if (nivel==2){
			dibujamapa2();
		}
		if (nivel==3){
			dibujamapa2();
		}
	}


	var canvas,ctx;
	function inicializa(){
		canvas=document.getElementById('miCanvas');
		ctx=miCanvas.getContext('2d');
		cargaImagenes();
	}
	var nom={{nombre}}
	console.log(nom)
	///-------------------------------------------
	//Bucle

	var FPS=50
	setInterval(function(){
		principal();
	},1000/FPS);

	function principal(){
		identificar_nivel(nivel);
		dibujaDer();
	}