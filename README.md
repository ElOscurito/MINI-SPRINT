# Mini-Sprint DevSecOps — Laboratorio U3_A4

Repositorio del proyecto integrador **Mini-Sprint DevSecOps** (Universidad Laica Eloy Alfaro de Manabí).

El objetivo de este laboratorio es simular un entorno ágil real (sprint corto) donde se hereda una API REST con deuda técnica y vulnerabilidades de seguridad intencionales, aplicando prácticas DevSecOps para identificar, priorizar, bloquear y remediar los hallazgos sin detener el ciclo de entrega de valor.

##  Estructura del Repositorio

```text
MINI-SPRINT/
├── api_rest_practica/          # Código fuente de la API REST vulnerable en Flask
│   ├── app.py                  # API Flask con endpoints de práctica
│   ├── requirements.txt        # Dependencias del escenario vulnerable
│   └── README.md               # Instrucciones de ejecución y análisis local
├── .gitignore                  # Exclusión de entornos virtuales, bases de datos y temporales
└── README.md                   # Documentación general del repositorio
```

##  Requisitos e Inicio Rápido

1. Dirígete a la carpeta del proyecto:
   ```powershell
   cd api_rest_practica
   ```
2. Crea y activa tu entorno virtual:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Instala las dependencias y herramientas de escaneo:
   ```powershell
   python -m pip install -r requirements.txt
   python -m pip install bandit pip-audit
   ```
4. Ejecuta la API:
   ```powershell
   python app.py
   ```

##  Herramientas de Seguridad

- **SAST (Bandit):**
  ```powershell
  bandit -r app.py -f txt
  ```
- **SCA (pip-audit):**
  ```powershell
  pip-audit -r requirements.txt
  ```

## Metodología DevSecOps

- **Backlog de Seguridad:** Gestionado mediante GitHub Issues y GitHub Projects.
- **Definition of Done (DoD):** Requiere revisión por pares mediante Pull Request y escaneo SAST en 0 alertas altas/medias antes de autorizar el merge a la rama principal.
