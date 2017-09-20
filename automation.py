
##########################################################################################################################################
#-------------------------------------------AUTOMATIZACION RESULTADOS ESTUDIO USUARIO FINAL----------------------------------------------
##########################################################################################################################################


#leer ficheros de log directamente de la carpeta donde estan almacenados

import sys
import glob
import errno
import json
import unicodedata


path = '/home/sandra/script_mixpanel/log/*.txt'
# glob.glob(path) encuentra todas las ocurrencias que se le pasen en el path 
files = glob.glob(path)   
for name in files:
    try:
        with open(name) as f: 
            #file=sys.stdout.write(f.read())
            file=f.read()
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise 

#me guardo los campos que me interesan: event, selection, component, version, user

jsonDatos = json.loads(file)
tam=len(jsonDatos)
nota=[]
eventos=[]
#eventos a eliminar por ser no numericos. Se han de tratar de forma diferente. Mineria de datos
evenDelete=['question5', 'question6','drawback','advantage']
#en events almaceno todos los eventos que no esten en la lista evenDelente
#events=[value for value in jsonDatos if not value['event'] in evenDelete]
#enumerate enumera los datos que se le pasan
for index,value in enumerate(jsonDatos):
	#hago un if para comprobar que los eventos no estan en la lista de elementos que tengo que eliminar por no ser numericos
	if not value['event'] in evenDelete:
		question=value['event']
		selection=value['properties']['selection']
		nota.append(int(selection))
		component=value['properties']['component']
		print component
		version=value['properties']['version']
		print version
		user=value['properties']['user']
	
	
	





	#HAGO IF COMPROBANDO SI EL EVENT ESTA DENTRO DE EVENTDELETE. AQUI LOS HE BORRADO. HAGO MEDIA DE LOS SELECTIONS (MAP REDUCE)
	#ELSE DE MOMENTO NO HAGO NADA. ANALISIS DE TEXTO (MINERIA DE DATOS)
	
	#convert unicode to str
	# events=unicodedata.normalize('NFKD', events).encode('ascii','ignore')
	