import requests

def main():
    while True:
        city = input("Введите название города (или 0 для выхода): ")
        if city == '0':
            print("Выход из программы.")
            break
        response = requests.post('http://server:5000/get_weather', json={'city': city})
        if response.status_code == 200:
            data = response.json()
            print(f"Погода в городе {data['city']} на {data['current_time']}:")
            print(f"Температура: {data['temp']}°C")
            print(f"Описание: {data['description']}")
            print(f"Влажность: {data['humidity']}%")
            print(f"Скорость ветра: {data['wind_speed']} м/с")
        else:
            print("Ошибка при получении данных о погоде.")

if __name__ == "__main__":
    main()

