import requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

API_KEY = 'здесь_ваш_ключ_из_сервиса_openweathermap.org'

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data['city']
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(base_url, timeout=5)
        weather_data = response.json()

        if response.status_code == 200:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result = {
                'city': city,
                'temp': temp,
                'description': description,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'current_time': current_time
            }
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Город не найден. Проверьте правильность названия.'}), 404

    except Exception as e:
        return jsonify({'error': f'Ошибка при получении данных: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
