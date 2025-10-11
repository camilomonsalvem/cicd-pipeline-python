"""
Aplicación Flask que actúa como calculadora básica.
Recibe datos desde un formulario HTML y realiza operaciones matemáticas
como sumar, restar, multiplicar y dividir.
"""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Función principal que maneja la calculadora.
    GET: muestra el formulario.
    POST: recibe datos del formulario, realiza la operación seleccionada.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operacion = request.form.get("operacion", "")

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Debes ingresar números válidos"
        except ZeroDivisionError:
            resultado = "No se puede dividir entre cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(port=5000, host="0.0.0.0")
