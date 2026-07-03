from flask import Flask, jsonify, request

app = Flask(__name__)

# Repositorio temporal de datos
# Esto no representa persistencia de datos
libros = (
    {
        101: { "id": "102", "titulo": "Clean code", "autor": "Robert C.", "disponible": True},
        102: { "id": "102", "titulo": "Python Crash", "autor": "Eric Matthes", "disponible": True},
        103: { "id": "103", "titulo": "Architiecture Patterns", "autor": "GoF", "disponible": True}
    }
)

@app.get("/")
def inicio():
    return jsonify(
        {
            "mensaje": "API REST de Biblioteca Universidad",
            "version": "1.0",
            "endpoints": [
                "GET /libros", #Muestra todos los libros
                "GET /libros/<id>", # Muestra UN libro
                "POST /libros", #Crea un nuevo libro
                "PUT /libros", #Modifica la disponibilidad
                "DELET /libros/<id>" # Borra un libro
            ]
        }
    )

@app.get("/libros")
def obtener_libros():
    return jsonify(list(libros.values()))

@app.get("/libros/<int:id>")
def obtener_un_libro(id):
    libro = libros.get(id)
    
    if libro:
        return jsonify(libro)
    
    return jsonify({"error": "Libro no encontrado"}), 404

@app.post("/libros")
def agregar_libro():
    datos = request.get_json()
    
    if not datos:
        return jsonify({"error": "Debe enviar informacion"}), 400
    if "titulo" not in datos or "autor" not in datos or "disponible" not in datos:
        return jsonify({"error": "los campos son requeridos"}), 400
    
    nuevo_id = max(libros.keys())+1 
    
    libros[nuevo_id]={
        "id": nuevo_id,
        "titulo": datos["titulo"],
        "autor": datos["autor"],
        "disponible": datos["disponible"]
    }
    
    return jsonify(libros[nuevo_id]), 201
    
if __name__ == "__main__":
    app.run(debug=True)