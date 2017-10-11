
##########################################################################################################################################
#-------------------------------------------AUTOMATIZACION RESULTADOS ESTUDIO USUARIO FINAL----------------------------------------------
##########################################################################################################################################


#leer ficheros de log directamente de la carpeta donde estan almacenados

import sys
import glob
import errno
import json
import unicodedata
import yaml
import os
from mongoengine import *

#abrir archivo configuracion
basepath = os.path.dirname(__file__)
configFile = os.path.abspath(os.path.join(basepath, "config.yaml"))
with open(configFile, "r") as ymlfile:
    config = yaml.load(ymlfile)

#poner array vacio sino existe el array de eventos a eliminar
if not config.has_key('eventsDelete'):
	config['eventsDelete']=[]

#salir del programa
if not config.has_key('logFiles') or not config.has_key('output'):
	print "fichero de configuracion debe contener logFiles y output"
	sys.exit()

if not config.has_key('DB') or not config.has_key('host') or not config.has_key('port') or not config.has_key('username') or not config.has_key('password'):
	print "datos insuficientes para la conexion a la base de datos"
	sys.exit()


#eventos a eliminar por ser no numericos. Se han de tratar bde forma diferente. Mineria de datos
#evenDelete=['question5', 'question6','drawback','advantage']

#crear estructura de datos con los componentes en formato:
#componente_version_pregunta: nota, usuario
estructura = {}

#copiar en un fichero la estructura de datos
#config['output'] = open('/home/sandra/Documentos/Labo/Feedback-final-users/Feedback.txt', 'w')


def sum_selections(estructura):
	#tengo que abrir primero el fichero para poder escribir posteriormente sobre el 
    with open(config['output'],"w") as file: 
		for clave, valor in estructura.iteritems():
			#declaro aqui la suma para que sean sumas diferentes por cada clave
			suma=0
			for lista_valores in valor:
				suma+=lista_valores['nota']
			media=suma/len(valor)
			print clave, media
			file.write( 'media de ' + clave + " = "+ str(media) + '\n' )

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
		if not rate['event'] in config['eventsDeleted']:
			question=rate['event']
			selection=rate['properties']['selection']
			component=rate['properties']['component']
			version_comp=rate['properties']['version']
			user=rate['properties']['user']
			estructura_datos(component,version_comp,question,selection,user)
	
#config['logFiles'] = '/home/sandra/script_mixpanel/log/*.txt'
# glob.glob(config['logFiles']) encuentra todas las ocurrencias que se le pasen en el path 

files = glob.glob(config['logFiles'])   
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


#conexion a la base de datos mongo
connect(config['DB'], host=config['host'], port=config['port'])
connect(config['DB'], username=config['username'], password=config['password'])


#peticiones la base de datos para meter las notas de los usuarios
