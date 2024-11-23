from database.base import Base
from database import db

class Incidente(Base):
    __tablename__ = 'incidente'

    id = db.Column(db.Integer, primary_key=True)
    ambiente = db.Column(db.String(50), nullable=False)
    cluster = db.Column(db.String(50), nullable=False)
    servico = db.Column(db.String(50), nullable=False)
    criticidade = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.String(50), nullable=False)