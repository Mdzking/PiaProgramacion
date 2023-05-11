import argparse
import subprocess

# Crear el objeto ArgumentParser
parser = argparse.ArgumentParser(description='Ejemplo de selección de script.')

# Agregar los argumentos
parser.add_argument('script', choices=['script1', 'script2', 'script3', 'script4'], help='Selecciona el script a ejecutar.')

# Obtener los argumentos de la línea de comandos
args = parser.parse_args()

# Verificar qué script se seleccionó y ejecutarlo
if args.script == 'script1':
    subprocess.call(['python', 'script1.py'])
elif args.script == 'script2':
    subprocess.call(['python', 'script2.py'])
elif args.script == 'script3':
    subprocess.call(['python', 'script3.py'])
elif args.script == 'script4':
    subprocess.call(['python', 'script4.py'])
