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

if __name__ == "__main__":
    app.run(debug=True)