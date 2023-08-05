# PyAirQuality

python3 -m venv paq

source paq/bin/activate

deactivate

docker build -t air .

docker run -dp 127.0.0.1:8050:8050 air

docker-compose build

docker-compose up -d

docker-compose down

pip3 install -r requirements.txt