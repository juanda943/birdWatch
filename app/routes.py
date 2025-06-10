
from flask import Blueprint, render_template, request, redirect
from app.controllers.avistamientos import (
    avistamientos, ultimos_avistamientos, NodoEspecie, arbol_especies,
    ordenar_por_fecha, ordenar_por_lugar
)

routes = Blueprint("routes", __name__)
arbol = None

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/registrar", methods=["GET", "POST"])
def registrar():
    global arbol_especies
    if request.method == "POST":
        especie = request.form["especie"]
        ubicacion = request.form["ubicacion"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        observador = request.form["observador"]
        comentario = request.form["comentario"]

        registro = {
            "especie": especie,
            "ubicacion": ubicacion,
            "fecha": fecha,
            "hora": hora,
            "observador": observador,
            "comentario": comentario
        }

        avistamientos.append(registro)
        ultimos_avistamientos.appendleft(registro)

        if arbol_especies is None:
            arbol_especies = NodoEspecie(especie)
            arbol_especies.registros.append(registro)
        else:
            arbol_especies.insertar(especie, registro)

        return redirect("/")
    return render_template("registrar.html")

@routes.route("/lista")
def lista():
    return render_template("lista.html", avistamientos=avistamientos, ultimos=list(ultimos_avistamientos))

@routes.route("/orden_fecha")
def orden_fecha():
    ordenados = ordenar_por_fecha(avistamientos)
    return render_template("lista.html", avistamientos=ordenados, ultimos=[])

@routes.route("/orden_lugar")
def orden_lugar():
    ordenados = ordenar_por_lugar(avistamientos)
    return render_template("lista.html", avistamientos=ordenados, ultimos=[])

@routes.route("/especies")
def especies():
    if arbol_especies:
        especies_ordenadas = arbol_especies.en_orden()
    else:
        especies_ordenadas = []
    return render_template("especie.html", especies=especies_ordenadas)
