
##########################################################################################################################################
#-------------------------------------------AUTOMATIZACION RESULTADOS ESTUDIO USUARIO FINAL----------------------------------------------
##########################################################################################################################################


#leer ficheros de log directamente de la carpeta donde estan almacenados

import sys
import glob
import errno

path = '/home/sandra/script_mixpanel/log/*.txt'
# glob.glob(path) encuentra todas las ocurrencias que se le pasen en el path 
files = glob.glob(path)   
for name in files:
    try:
        with open(name) as f: 
            sys.stdout.write(f.read())
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise 


#me guardo los campos que me interesan: event, selection, component, version, user

