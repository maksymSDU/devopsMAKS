from flask import Flask, render_template
import redis
import threading

app = Flask(__name__)

# Подключаемся к Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Функция для подписки на Redis канал
def listen_to_redis():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('my_channel')
    for message in pubsub.listen():
        print(f"Received message: {message['data']}")

# Запуск подписки в отдельном потоке
thread = threading.Thread(target=listen_to_redis)
thread.daemon = True
thread.start()

@app.route('/')
def index():
    return "Hello from Flask, waiting for Redis messages..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template
import redis
import threading

app = Flask(__name__)

# Подключаемся к Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Функция для подписки на Redis канал
def listen_to_redis():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('my_channel')
    for message in pubsub.listen():
        print(f"Received message: {message['data']}")

# Запуск подписки в отдельном потоке
thread = threading.Thread(target=listen_to_redis)
thread.daemon = True
thread.start()

@app.route('/')
def index():
    return "Hello from Flask, waiting for Redis messages..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



from flask import Flask, render_template
import redis
import threading

app = Flask(__name__)

# Подключаемся к Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Функция для подписки на Redis канал
def listen_to_redis():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('my_channel')
    for message in pubsub.listen():
        print(f"Received message: {message['data']}")

# Запуск подписки в отдельном потоке
thread = threading.Thread(target=listen_to_redis)
thread.daemon = True
thread.start()

@app.route('/')
def index():
    return "Hello from Flask, waiting for Redis messages..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
