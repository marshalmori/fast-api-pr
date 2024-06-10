# JWT_SECRET = config('JWT_SECRET')
from typing import ClassVar

from decouple import config
#pip install pydantic_settings
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = config('DB_URL')
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()

    JWT_SECRET: str = config('JWT_SECRET')

    """
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()

