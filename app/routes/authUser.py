from fastapi import APIRouter, Depends

from app.core.jwt_auth import verificar_token

router = APIRouter()


@router.post("/perfil")
def perfil(usuario = Depends(verificar_token)):

    return {

        "status": "accept",

        "usuario": usuario
    }