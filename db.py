# Conexion a la base de datos

# importamos la libreria para usar las herramientas 
import pymongo 

# Creamos la conexion con el puerto de la bd
client = pymongo.MongoClient("localhost", 27017)

# Creamos la base
db = client["MateriasGracosoft"]

# creamos la colecion de datos
collection = db["materias"]