"""API de laboratorio con vulnerabilidades intencionales. Solo para uso local."""
import sys
if sys.version_info >= (3, 14):
    import pkgutil, importlib.util, ast
    if not hasattr(pkgutil, 'get_loader'):
        def _get_loader(name):
            mod = sys.modules.get(name)
            if mod and hasattr(mod, '__loader__') and mod.__loader__ is not None:
                return mod.__loader__
            try:
                spec = importlib.util.find_spec(name)
                return spec.loader if spec else None
            except Exception:
                return None
        pkgutil.get_loader = _get_loader
    if not hasattr(ast, 'Str'):
        class StrShim(ast.Constant):
            def __init__(self, s, **kwargs):
                super().__init__(value=s, **kwargs)
            @property
            def s(self):
                return self.value
            @s.setter
            def s(self, val):
                self.value = val
        ast.Str = StrShim

from flask import Flask, jsonify, request
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("practica.db")
API_KEY = "API_KEY_DEMO_NO_USAR_EN_PRODUCCION"


def init_db():
    """Crea datos ficticios para probar el endpoint de autenticación."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users "
            "(id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        )
        conn.execute(
            "INSERT OR IGNORE INTO users (id, username, password) VALUES "
            "(1, 'admin', 'AdminDemo123!'), (2, 'estudiante', 'Practica123!')"
        )


@app.get("/api/health")
def health():
    return jsonify(status="ok", service="API de práctica")


@app.get("/api/profile")
def profile():
    # Vulnerabilidad intencional: secreto fijo en el código.
    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify(error="No autorizado"), 401
    return jsonify(user="admin", message="Acceso de demostración")


@app.post("/api/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    # Vulnerabilidad intencional: SQL concatenado con datos del usuario.
    query = (
        "SELECT id, username FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(query).fetchone()

    if row:
        return jsonify(message="Login correcto", user={"id": row[0], "username": row[1]})
    return jsonify(error="Credenciales inválidas"), 401


if __name__ == "__main__":
    init_db()
    # Escucha solo en localhost. No publicar esta API vulnerable en Internet.
    app.run(host="127.0.0.1", port=5000, debug=False)