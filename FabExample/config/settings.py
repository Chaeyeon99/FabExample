import os

class Settings:
    ENVIRONMENT = "development"
    DEBUG = True
    SECRET_KEY = os.getenv("FAB_SECRET", "defaultsecretkey")
    DB_URL = f"postgresql://fabadmin:fabpass2024@localhost:5432/fabexample_db"
    AWS_REGION = "ap-northeast-2"
    LOG_LEVEL = "INFO"
