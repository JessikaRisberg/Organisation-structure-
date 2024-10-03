# Använd en officiell Python-bild som bas
FROM python:3.12

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera requirements.txt till containern
COPY requirements.txt .

# Installera Python-paketen som anges i requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera den återstående koden till containern
COPY . .

# Ange kommandot för att köra din applikation
CMD ["python", "main.py"]