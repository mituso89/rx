import os


class Config:
    queue = os.getenv("QUEUE")
    port = os.getenv("PORT")
    mariadb_master_url = os.getenv('MARIADB_MASTER_URL')
    redis_host = os.getenv('REDIS_HOST')
    redis_password = os.getenv('REDIS_PASSWORD')
    redis_db = os.getenv('REDIS_DB')
    redis_prefix = os.getenv('REDIS_PREFIX')
    aws_region = os.getenv('AWS_REGION')
    redis_port = os.getenv('REDIS_PORT')
    queue = os.getenv('QUEUE')
    email = os.getenv('EMAIL')
    stmp_username = os.getenv('SMTP_USERNAME')
    stmp_password = os.getenv('SMTP_PASSWORD')
    stmp_host = os.getenv('SMTP_HOST')
    email_to = os.getenv('EMAIL_TO')
    maria_host = os.getenv('MARIA_HOST')
    maria_db = os.getenv('MARIA_DB')
    maria_user = os.getenv('MARIA_USER')
    maria_pass = os.getenv('MARIA_PASS')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
