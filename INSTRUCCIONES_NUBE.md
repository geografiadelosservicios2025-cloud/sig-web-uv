# Guía para Publicar tu SIG Web en Internet

Para que cualquier persona pueda acceder, sigue estos pasos:

## Opción Recomendada: Render.com (Gratis)

1. **Subir a GitHub**:
   - Crea un repositorio en GitHub.
   - Sube todos los archivos de esta carpeta.

2. **Crear Servicio en Render**:
   - Ve a `https://dashboard.render.com/`
   - New + -> Web Service.
   - Conecta tu GitHub y elige el repo.

3. **Configuración CRÍTICA**:
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

---

## Comandos para probar antes de subir:
- `pip install -r requirements.txt` (Instala las librerías)
- `python main.py` (Ejecuta el servidor localmente)

---
*Nota: El archivo main.py ya está configurado para leer el puerto dinámico ($PORT) de Render.*
