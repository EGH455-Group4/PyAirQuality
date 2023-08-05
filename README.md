# PyAirQuality

### Python commands

python3 main.py

### Virtual env commands

python3 -m venv paq

source paq/bin/activate

deactivate

### Python install commands

pip3 install -r requirements.txt

pip3 freeze > requirements.txt

### Docker commands

docker build -t air .

docker run -dp 127.0.0.1:8050:8050 air

docker-compose build

docker-compose up -d

docker-compose down
