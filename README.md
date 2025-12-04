# Meme Generator

Dockerizirana aplikacija koja omogućava generisanje meme-a sa gornjim i donjim tekstom.

## Pokretanje

1. Build Docker image:
docker build -t meme-generator:latest .

2. Pokretanje kontejnera:
docker run -d -p 5000:5000 --name meme-run -v "${PWD}/static:/app/static" meme-generator:latest

3. Otvoriti u browseru:
http://127.0.0.1:5000

