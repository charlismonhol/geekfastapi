from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings


class ArtigoModel(settings.DBBaseModel):
    __tablename__: str = 'artigos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(256))
    url_fonte: str = Column(String(256))
    descricao: str = Column(String(256))
    usuario_id: int = Column(Integer, ForeignKey('usuarios.id'))
    
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')