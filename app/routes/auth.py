from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.usuario import Usuario
from app.schemas.auth_schema import Register, Login

from app.models.token import Token
from datetime import datetime, timedelta

from app.core.security import (
    gerar_hash,
    verificar_senha,
    criar_token
)

router = APIRouter()


@router.post("/login")
def login(dados: Login):

    db: Session = SessionLocal()

    usuario = db.query(Usuario).filter(
        Usuario.email == dados.user
    ).first()

    if not usuario:

        db.close()

        return {
            "status": "error",
            "mensagem": "Usuário não encontrado"
        }

    senha_correta = verificar_senha(
        dados.pass2,
        usuario.senha
    )

    if not senha_correta:

        db.close()

        return {
            "status": "error",
            "mensagem": "Senha incorreta"
        }


    token = criar_token({

        "sub": usuario.usuario,
        "id": usuario.id

    })

    expiracao = datetime.utcnow() + timedelta(seconds=3600)

    novo_token = Token(

        usuario_id = usuario.id,

        token = token,

        expiracao = expiracao
    )

    db.add(novo_token)

    db.commit()
    
    nome_usuario = usuario.usuario

    db.close()

    return {

        "status": "accept",

        "token": token,

        "usuario": nome_usuario
    }


@router.post("/register")
def register(dados: Register):

    db: Session = SessionLocal()

    email = db.query(Usuario).filter(
        Usuario.email == dados.reg_email
    ).first()

    user = db.query(Usuario).filter(
        Usuario.usuario == dados.reg_user
    ).first()

    if email:

        db.close()

        return {
            "status": "aviso",
            "mensagem": "Email já cadastrado"
        }

    if user:

        db.close()

        return {
            "status": "aviso",
            "mensagem": "Usuário já existe"
        }

    newUser = Usuario(

        usuario=dados.reg_user,

        email=dados.reg_email,

        senha=gerar_hash(
            dados.reg_pass
        )
    )

    db.add(newUser)

    db.commit()

    db.close()

    return {
        "status": "accept",
        "mensagem": "Registro realizado"
    }