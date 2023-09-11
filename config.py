from decouple import config

host = config('MONGODB_HOST')
port = config('MONGODB_PORT')
username = config('MONGODB_USERNAME')
password = config('MONGODB_PASSWORD')
database = config('MONGODB_DATABASE')