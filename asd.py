
hola = 'hola,como,estas'
# with open("Database.txt","a+") as db:
#     datos = db.write('texto,a,escribir')

with open("Database.txt") as db:
	efe = db.readlines()

for i in range(len(efe)):
    a = i + 1
    if a > len(efe):
        print(a)
        db.writelines(efe+'\n'+hola)
        print(efe+'\n'+hola)

print(efe)

def top_5(alumnos):
    '''
    Con esta función se busca entre todos los alumnos registrados cuáles son los 5 con mejores promedios.

    Argumentos => alumnos: lista de alumnos ya registrados.

    Retorna: => los 5 alumnos con mejores promedios con su promedio y el grado que cursa.

    '''
    
    # para este sort se usa como key una lambda function, con esto se hace que la lista se organice según el promedio de los alumnos. El reverse se usa para indicar que se quiere de mayor a menor (sin el reverse sería de menor a mayor)
    alumnos.sort(key = lambda alumno: alumno.promedio, reverse=True)
    for i,alumno in enumerate(alumnos):
        if i < 5:
            print("---",i+1,"---------------")
            print(alumno.mostrar())


