# Importar Flask
from flask import Flask, render_template, redirect, url_for, request

# Crear la aplicación
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el botón 1
@app.route('/boton1')
def boton1():
    return render_template('notas.html')

# Ruta para el botón 2
@app.route('/boton2')
def boton2():
    return render_template('nombre.html')

#proceso de promediar notas

@app.route('/', methods=['GET'])
def notass():
    return render_template('index.html')

@app.route('/notas', methods=['POST'])
def notas():
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])
    asistencia = float(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        estado = 'Aprobado'
    else:
        estado = 'Reprobado'

    return render_template('notas.html', promedio=promedio, estado=estado)

#DEVOLUCION DE NOMBRES

@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    if request.method == 'POST':
        # Procesa la solicitud POST
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        nombre_mas_largo = max(nombres, key=len)
        cantidad_letras = len(nombre_mas_largo)

        return render_template('nombre.html', nombre_mas_largo=nombre_mas_largo, cantidad_letras=cantidad_letras)
    else:
        return render_template('nombre.html')


if __name__ == '__main__':
    app.run(debug=True)

