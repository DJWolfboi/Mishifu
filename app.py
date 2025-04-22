from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Simple TODO API"

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'aplicacion': 'Servidor Flask Demo',
        'version': '1.0',
        'autor': 'Noel'
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    nombre = data.get('nombre', 'usuario')
    return jsonify({'respuesta': f'Hola, {nombre}. Tu mensaje fue recibido correctamente.'})

if __name__ == '__main__':
    app.run(debug=True)
