from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__: str = 'usuarios'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(256), nullable=True)
    sobrenome: str = Column(String(256), nullable=True)
    email: str = Column(String(256), index=True,  nullable=False, unique=True)
    senha: str = Column(String(256), nullable=False)
    eh_admin: Boolean = Column(Boolean, default=False)

    artigos = relationship("ArtigoModel", cascade= "all, delete-orphan", back_populates="criador", uselist=True, lazy='joined')
    

    , Field