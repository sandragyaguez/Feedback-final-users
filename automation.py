
##########################################################################################################################################
#-------------------------------------------AUTOMATIZACION RESULTADOS ESTUDIO USUARIO FINAL----------------------------------------------
##########################################################################################################################################


#leer ficheros de log directamente de la carpeta donde estan almacenados

import sys
import glob
import errno
import json
import unicodedata

#eventos a eliminar por ser no numericos. Se han de tratar de forma diferente. Mineria de datos
evenDelete=['question5', 'question6','drawback','advantage']

#crear estructura de datos con los componentes en formato:
#componente_version_pregunta: nota, usuario
estructura = {}

def sum_selections(estructura):
	for clave, valor in estructura.iteritems():
		#declaro aqui la suma para que sean sumas diferentes por cada clave
		suma=0
		for lista_valores in valor:
			suma+=lista_valores['nota']
		media=suma/len(valor)
		print clave, media

def estructura_datos(componente,version,pregunta,nota,usuario):
	key = str(componente + "_" + version + "_" + pregunta)
	#comprobar que la estructura no tiene ese dato. Si lo tiene se almacena donde estaba (el valor) y sino se crea
  	if not key in estructura:
  		estructura[key] = []

	value= {"nota": int(nota), "usuario":str(usuario)}
	estructura[key].append(value)
	

#me guardo los campos que me interesan: event, selection, component, version, user
def parse_file(file):
	jsonDatos = json.loads(file)
	for rate in jsonDatos:
		#hago un if para comprobar que los eventos no estan en la lista de elementos que tengo que eliminar por no ser numericos
		if not rate['event'] in evenDelete:
			question=rate['event']
			selection=rate['properties']['selection']
			component=rate['properties']['component']
			version_comp=rate['properties']['version']
			user=rate['properties']['user']
			estructura_datos(component,version_comp,question,selection,user)
	
path = '/home/sandra/script_mixpanel/log/*.txt'
# glob.glob(path) encuentra todas las ocurrencias que se le pasen en el path 
files = glob.glob(path)   
for name in files:
    try:
        with open(name) as f: 
            file=f.read()
            parse_file(file)
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise 

print estructura
sum_selections(estructura)



#copiar en un fichero la estructura de datos
file = open('/home/sandra/Documentos/Labo/Feedback-final-users/Feedback.txt', 'w')
file.write('This is a test') 
file.close()
	





	#HAGO IF COMPROBANDO SI EL EVENT ESTA DENTRO DE EVENTDELETE. AQUI LOS HE BORRADO. HAGO MEDIA DE LOS SELECTIONS (MAP REDUCE)
	#ELSE DE MOMENTO NO HAGO NADA. ANALISIS DE TEXTO (MINERIA DE DATOS)
	
	#convert unicode to str
	# events=unicodedata.normalize('NFKD', events).encode('ascii','ignore')
	