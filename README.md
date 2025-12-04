# Meme Generator

Dockerizirana aplikacija katera omogoca generiranje meme-a z spodnjim in zgornjim besedilom.

## Zagon

1. Build Docker image:
docker build -t meme-generator:latest .

2. Zagon kontejnerja:
docker run -d -p 5000:5000 --name meme-run meme-generator:latest

3. Odpiranje v brskalniku:
http://127.0.0.1:5000

