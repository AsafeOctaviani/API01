from fastapi import APIRouter, Depends
from models import Usuario
from dependecies import pegar_sessao
from main import bcrypt_context


auth_router=APIRouter(prefix="/auth",tags=["authentication"])

@auth_router.get("/")

async def home():
    """
    Essa é a rota padrão de autenticação para o sitema
    """
    return {"mensagem":"você acessou a rota de autenticação","authenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(email:str,senha:str,nome:str,session= Depends(pegar_sessao)):
    
    usuario=session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return{"mensagme":"Já existe um usuário com esse email"}
    
    else:
        senha_criptografada=bcrypt_context.hash(senha)
        novo_usuario=Usuario(nome,email,senha_criptografada)
        session.add(novo_usuario)
    session.commit()
        return {f"mensagem":"Usuario cadastrado com sucesso"}

