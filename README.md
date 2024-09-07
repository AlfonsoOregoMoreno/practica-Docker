# Microservicio de conteo de visitas

Práctica correspondiente al Módulo de Docker del Bootcamp DevOps-10 de Keepcoding.

Se compone de 2 contenedores: 
· uno con una app en python/flask, que levanta un server HTTP escuchando peticiones GET por el end-point "/increment", a modo de contador de visitas.
· otro con una BDD postgres donde se almacena el contador de visitas.

## Instalación

Linux, y Windows con Docker-Desktop:

· 1) Nos posicionamos en la ruta base del proyecto:
```sh
cd version01/
```

· 2) Construcción de la imagen de la app:
```sh
cd flask-app/
sudo docker image build .
sudo docker compose build
cd ..
```
Eso usará el fichero "Dockerfile" del DIR "flask-app/" para generar la imagen de la app de python/flask

· 3) Composición del microservicio:
```sh
sudo docker compose build
```
Eso usará el fichero "docker-compose.yml" de la ruta base del proyecto para componser los servicios (app y BDD).

· 4) Arranque del microservicio:
```sh
sudo docker compose up
```
El resultado es que se arrancan los contenedores, y la app estará escuchando por el puerto interno indicado por configuración (ahora el 6002), pero expuesto hacia afuera por el 5000. 

## Ejemplo para testeo

· Desde otra terminal/consola:
```sh
curl http://localhost:5000/increment
```
Eso debe devolver un pequeño JSON conteniendo solo un objeto con la propiedad "count" y el valor correspondiente. 
Ej. de objeto devuelto: {"count":305}

· Comando Linux que ayuda a ver el funcionamiento en tiempo real, haciendo peticiones cada 1 seg.:
```sh
watch -n1 'curl http://localhost:5000/increment'
```


## Meta

Autor: Alfonso Orego
E-mail: alfonso.orego.moreno@gmail.com
Ruta pública al Repo: https://github.com/AlfonsoOregoMoreno/practica-Docker


