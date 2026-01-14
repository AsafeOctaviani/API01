from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db= create_engine("sqlite:///banco.db")

Base= declarative_base()

class Usuario(Base):
    __tablename__= "Users" #__table__name é usado para definir o nome da minha tabela
    #após definir o nome você define os campos
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    name= Column("name",String,nullable=False)
    email = Column("email",String,nullable=False)
    senha= Column("pass",String,nullable=False)
    activity= Column("activity",Boolean,nullable=False)
    admin= Column("admin",Boolean,nullable=True,default=False)


    def __init__(self,name,email,senha,activity = True,admin=False):
        self.name=name
        self.email=email
        self.senha=senha
        self.activity=activity
        self.admin=admin

class Order(Base):
    __tablename__="Orders"

    # ORDER_STATUS = (
    #     #(key,value)
    #     #key é armazenada no database
    #     #é o texto da key
    #     ("PENDENTE","PENDENTE"),
    #     ("CANCELADO","CANCELADO"),
    #     ("FINALIZADO","FINALIZADO")
    #     )

    #("nome",tipo,configuração)
    id=Column("id",Integer,primary_key=True,autoincrement=True)
    status=Column("status",String) #pendene/canclado/finalizado
    user=Column("user",ForeignKey("Users.id"))
    #Quando campo da sua tabela recebe um item de outra tabela você usa o ForeingKey
    #para sinalizar que é uma chave estrangeira
    price=Column("price",Float,)
    #itens=Column(String)

    def __init__(self,user,status="PENDENTE",price=0):
        self.user=user
        self.status=status
        self.price=price


class Item(Base):
    __tablename__="Itens"
    id=Column("id",Integer,primary_key=True,autoincrement=True)
    quantity=Column("quantity",Integer)
    size=Column("size",String)
    flavor=Column("flavor",String)
    unit_price=Column("unit_price",Float)
    order=Column("order",ForeignKey("Orders.id"))

    def __init__(self,quantity,size,flavor,unit_price,order):
        self.quantity=quantity
        self.size=size
        self.flavor=flavor
        self.unit_price=unit_price
        self.order=order