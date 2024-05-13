# J. M. J. - Proyecto Base de datos II - Grabriel Cuervo - Gracosoft - 31/05/24

# Servicios de la aplicacion

# Importamos las librerias
from flask import Flask, request, render_template, redirect, url_for, flash 
from bson.objectid import ObjectId
from db import collection

# Creamos una instancia de la clase Flask y configuramos la clave de la aplicacion
app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "Doofenshmirtz"

# Metodos de la aplicacion:

# -Metodo: Obtener lista de elementos
@app.route("/list", methods=["GET"])
def getSubjets():
    elementsList = collection.find()

    return render_template('materias.html.jinja', elementsList=elementsList)