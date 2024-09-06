# Usa una imagen base de Python
FROM python:3.7-alpine

# Copia el archivo requirements.txt y el código de la aplicación al contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala las dependencias
RUN pip install -r requirements.txt

ENV FLASK_APP_CONTAINER_EXPOSED_PORT=6002

# Expone el puerto de la app
EXPOSE $FLASK_APP_CONTAINER_EXPOSED_PORT

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
