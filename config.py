from dotenv import load_dotenv
import os

load_dotenv() #Когда мы вызываем эту функцию без параметров,
#запускается функыия find_dotenv() которая ищет файл .env и загружает данные в переменные окружения

print('os env=', os.environ)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
