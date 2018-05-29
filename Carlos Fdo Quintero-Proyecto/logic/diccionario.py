import os
filepath1=os.path.abspath(os.getcwd()) + '/logic/preguntas.txt'
filepath2=os.path.abspath(os.getcwd()) + '/logic/opciones.txt'
filepath3=os.path.abspath(os.getcwd()) + '/logic/respuestas.txt'
filepath4=os.path.abspath(os.getcwd()) + '/logic/preguntastomadas.txt'
def getQuestions(grado):
  f=open(filepath1, "r")
  l_preguntas_por_grado=[ ]
  nombre_cursos=[ ]
  f.readline()
  for line in f:
    line=line.replace("\n"," ")
    sub_list=line.split(",")
    if int(sub_list[2])==grado:
      l_preguntas_por_grado.append(sub_list)
      if not sub_list[1] in nombre_cursos:
        nombre_cursos.append(sub_list[1])
  f.close()
  return [l_preguntas_por_grado,nombre_cursos]

def getOptions(list_questions):
  f=open(filepath2,"r")
  all_options=[ ]
  f.readline()
  for line in f:
    line=line.replace("\n", " ")
    sub_list=line.split(",")
    all_options.append(sub_list)
  f.close()
  options=[ ]
  ids_list=[ ]
  for question in list_questions:
    id_=question[0]
    sub_list=[ ]
    for option in all_options:
      if int(option[1])==int(id_):
        sub_list.append(option[2])
    ids_list.append(id_)
    options.append(sub_list)
  return [options, ids_list ]

def getAnswers():
  f=open(filepath3,"r")
  f.readline()
  id_questions=[]
  answers=[]
  for line in f:
    line=line.replace("\n"," ")
    sub_list=line.split(",")
    id_questions.append(int(sub_list[0]))
    answers.append(int(sub_list[1]))
  f.close()
  return [answers, id_questions]

def getQuestionViewed(userId):
  f=open(filepath4,"r")
  f.readline()
  id_questions=[]
  for line in f:
    line=line.replace("\n", "")
    sub_list=line.split(",")
    if str(sub_list[1])==str(userId):
      id_questions.append(int(sub_list[0]))
  f.close()
  return id_questions

def joinTables(tbl_questions,l_question_viewed):
  for id_question in l_question_viewed:
    for fila in range (len(tbl_questions)):
      if int(tbl_questions[fila][0])==int(id_question):
        tbl_questions.pop(fila)
        break
  return tbl_questions


def getCourseDiccionary(correo,grade):
  data=getQuestions(grade)
  list_questions=data[0]
  list_questions_viewed=getQuestionViewed(correo)
  list_questions=joinTables(list_questions,list_questions_viewed)
  courses_name=data[1]
  questions=[ ]
  print(list_questions_viewed)
  
  [options,id_questions]=getOptions(list_questions)
  [answers,id_questions2]=getAnswers()
  for course_name in courses_name:
    course={ }
    course["nombre"]= course_name
    course["grado"]=grade
    all_questions=[ ]
    id_question=[ ]
    list_options=[ ]
    list_answers= [ ]
    for question in list_questions:
      if question[1]==course_name:
        all_questions.append(question[3])
        id_question.append(int(question[0]))
        list_options.append(options[id_questions.index(question[0])])
        list_answers.append(answers[id_questions2.index(int(question[0]))])
    course["questions"]=all_questions
    course["id_questions"]=id_question
    course["opciones"]= list_options
    course["respuestas"]=list_answers
    if len(course["questions"])>0:
      questions.append(course)
      
  return questions
print(getCourseDiccionary("CarlosQ",0))
