"""
Aplicación Flask que actúa como calculadora básica.
Recibe datos desde un formulario HTML y realiza operaciones matemáticas
como sumar, restar, multiplicar, dividir, potencia y módulo.
"""

import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir, potencia, modulo

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Función principal de la aplicación.
    Maneja las solicitudes GET para mostrar el formulario y POST
    para procesar las operaciones de la calculadora.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            elif operacion == "potencia":
                resultado = potencia(num1, num2)
            elif operacion == "modulo":
                resultado = modulo(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    """Endpoint de verificación de salud para el ALB."""
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    app_port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=app_port, debug=False)
