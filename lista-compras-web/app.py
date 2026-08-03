from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Bases de datos temporales (en memoria)
productos = []
lista_compras = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/productos', methods=['GET', 'POST', 'DELETE'])
def manejar_productos():
    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        if nombre and nombre not in productos:
            productos.append(nombre)
        return jsonify({'status': 'ok'})
    elif request.method == 'DELETE':
        data = request.get_json()
        nombre = data.get('nombre')
        if nombre in productos:
            productos.remove(nombre)
        return jsonify({'status': 'ok'})
    return jsonify(productos)

@app.route('/api/lista', methods=['GET', 'POST', 'DELETE'])
def manejar_lista():
    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre')
        if nombre and nombre not in lista_compras:
            lista_compras.append(nombre)
        return jsonify({'status': 'ok'})
    elif request.method == 'DELETE':
        data = request.get_json()
        nombre = data.get('nombre')
        if nombre in lista_compras:
            lista_compras.remove(nombre)
        return jsonify({'status': 'ok'})
    return jsonify(lista_compras)

if __name__ == '__main__':
    app.run(debug=True)