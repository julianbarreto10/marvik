#!/bin/bash

pip3 install -r requirements.txt
uvicorn main:app --reload

#Ejemplos de Peticiones
#Prueba del endpoint POST /get-date/:

curl -X POST "http://127.0.0.1:8000/get-date/" -H "Content-Type: application/json" -d "{\"detailed\": true}"

#Prueba del endpoint GET /counter/:
curl -X GET "http://127.0.0.1:8000/counter/"