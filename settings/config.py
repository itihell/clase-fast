from pydantic import BaseSettings
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    USER_DATA_DASE: str = os.getenv('USER_DATA_DASE')
    PASSWORD_DATA_BASE: str = os.getenv('PASSWORD_DATA_BASE')
    PORT_DATA_BASE: str = os.getenv('PORT_DATA_BASE')
    NAME_DATA_BASE: str = os.getenv('NAME_DATA_BASE')
    HOST_DATA_BASE: str = os.getenv('HOST_DATA_BASE')
    SQLALCHEMY_DATABASE_URL: str = f"postgresql://{USER_DATA_DASE}:{PASSWORD_DATA_BASE}@{HOST_DATA_BASE}:{PORT_DATA_BASE}/{NAME_DATA_BASE}"


settings = Settings()
