
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
#eventos a eliminar
evenDelete=['drawback','advantage']

#recorro la lista buscando drawback y advantage con la lista que me he creado arriba y elimino. PREGUNTAR MIGUEL

for index,value in enumerate(jsonDatos):
	print index,value
	
	# events=x['event']
	# #convert unicode to str
	# events=unicodedata.normalize('NFKD', events).encode('ascii','ignore')
	# eventos.append(events)
	# #elimino las dos ultimas preguntas ya que no son valores numericos
	# even=eventos[:-2]
	# selection=x['properties']['selection']
	# print selection
	# #nota.append(int(selection))
	# component=x['properties']['component']
	# #print component
	# version=x['properties']['version']
	# #print version
	# user=x['properties']['user']
	# #print user
	# #print "--------------------------------------------------------------------"