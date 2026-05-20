from jose import jwt, JWTError
from fastapi import Header, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.token import Token
from app.core.security import SECRET_KEY, ALGORITHM


def verificar_token(authorization: str = Header(None)):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Token não enviado"
        )

    try:

        token = authorization.replace("Bearer ", "")

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        db: Session = SessionLocal()

        token_db = db.query(Token).filter(
            Token.token == token
        ).first()

        db.close()

        if not token_db:

            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )