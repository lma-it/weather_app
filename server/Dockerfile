# Используем базовый образ Python
FROM python:3.9

# Устанавливаем необходимые библиотеки
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем серверный код в контейнер
COPY server.py ./

# Устанавливаем точку входа
CMD ["python", "server.py"]
