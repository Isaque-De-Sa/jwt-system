from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "super_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_SECOND = 3600

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def gerar_hash(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha, hash):
    return pwd_context.verify(senha, hash)

def criar_token(data: dict):

    dados = data.copy()

    expire = datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECOND)

    dados.update({
        "exp": expire
    })

    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)