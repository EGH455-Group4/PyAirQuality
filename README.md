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

### Other
@reboot bash /home/tom/PyAirQuality/set_ip.sh

### lcd screen
curl -X POST http://127.0.0.1:8050/lcd-screen -H 'Content-Type: application/json' -d '{"display": "temperature"}'

curl -X POST http://127.0.0.1:8050/lcd-screen -H 'Content-Type: application/json' -d '{"display": "image_processing"}'

curl -X POST http://127.0.0.1:8050/lcd-screen -H 'Content-Type: application/json' -d '{"display": "IP_address"}'
