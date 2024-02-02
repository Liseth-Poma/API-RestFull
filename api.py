from flask import Flask, request, jsonify

app = Flask(_name_)

# Datos de inicio con un ID autoincremental
mantenimiento_vias_data = [
    {
        "id": 1,
        "ubicacion": "Carretera Panamericana Sur",
        "tipo": "Mantenimiento preventivo",
        "inicio": "2024-04-01",
        "fin": "2024-04-15"
    }
]
id_counter = 2  # Inicializar el contador de IDs

# Rutas CRUD
@app.route('/api/v1/mantenimiento_vias', methods=['GET'])
def obtener_mantenimientos():
    return jsonify({"mantenimiento_vias": mantenimiento_vias_data})

@app.route('/api/v1/mantenimiento_vias', methods=['POST'])
def agregar_mantenimiento():
    global id_counter
    nuevo_mantenimiento = request.json
    nuevo_mantenimiento["id"] = id_counter
    id_counter += 1
    mantenimiento_vias_data.append(nuevo_mantenimiento)
    return jsonify({"mensaje": "Mantenimiento agregado exitosamente"})

@app.route('/api/v1/mantenimiento_vias/<int:mantenimiento_id>', methods=['GET'])
def obtener_mantenimiento(mantenimiento_id):
    mantenimiento = next((m for m in mantenimiento_vias_data if m['id'] == mantenimiento_id), None)
    return jsonify({"mantenimiento": mantenimiento})

@app.route('/api/v1/mantenimiento_vias/<int:mantenimiento_id>', methods=['PUT'])
def actualizar_mantenimiento(mantenimiento_id):
    nuevo_mantenimiento = request.json
    for mantenimiento in mantenimiento_vias_data:
        if mantenimiento['id'] == mantenimiento_id:
            mantenimiento.update(nuevo_mantenimiento)
            return jsonify({"mensaje": "Mantenimiento actualizado exitosamente"})
    return jsonify({"error": "Mantenimiento no encontrado"}), 404

@app.route('/api/v1/mantenimiento_vias/<int:mantenimiento_id>', methods=['DELETE'])
def eliminar_mantenimiento(mantenimiento_id):
    global mantenimiento_vias_data
    mantenimiento_vias_data = [m for m in mantenimiento_vias_data if m['id'] != mantenimiento_id]
    return jsonify({"mensaje": "Mantenimiento eliminado exitosamente"})

# Punto de entrada
if _name_ == '_main_':
    app.run(debug=true)