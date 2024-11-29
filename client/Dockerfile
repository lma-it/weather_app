# Используем базовый образ Python
FROM python:3.9

# Устанавливаем необходимые библиотеки
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем клиентский код в контейнер
COPY client.py ./

# Устанавливаем точку входа
CMD ["python", "client.py"]
