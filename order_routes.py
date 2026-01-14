from fastapi import APIRouter

order_router = APIRouter(prefix="/orders",tags=["orders"])

# @order_router.get("/lista")
@order_router.get("/")
async def order_function():
    """
    Essa é a rota padrão para pedidos do sistema
    """
    return {"mensagem": "Você acessou a rota de pedidos"}