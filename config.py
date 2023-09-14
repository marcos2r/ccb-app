from decouple import config

# Use as variáveis do seu arquivo .env para construir a mongodb_uri
mongodb_uri = config('MONGODB_URL')
mongodb_name = config('MONGODB_NAME')