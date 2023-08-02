from typing import List

from pydantic import BaseSettings, Field as PydanticField
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:123456@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'C-wX3m-CfKdGD08tXAiqYH7hFGcKBskjjQdaExgiBuI'
    """
    abrir o terminal python para gerar o token
        import secrets 
        token: str = secrets.token_urlsafe(32)
        token
        C-wX3m-CfKdGD08tXAiqYH7hFGcKBskjjQdaExgiBuI
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 hors * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()