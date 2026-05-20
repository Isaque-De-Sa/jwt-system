from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class Token(Base):

    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id")
    )

    token = Column(String(500), nullable=False)

    criado_em = Column(
        DateTime,
        default=datetime.utcnow
    )

    expiracao = Column(DateTime, nullable=False)