from fastapi import FastAPI, Request,Response
from sqlmodel import Field, Session, SQLModel, create_engine, select, delete

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from db import Product, create_db_and_tables, engine, readAllProducts, createProduct, deleteProduct

app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


templates = Jinja2Templates(directory="templates")
@app.get("/seeproducts", response_class=HTMLResponse)
async def read_item(request: Request,search:str=''):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"productsList": readAllProducts(search)}
    )
##########################################################

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
async def getProducts(search:str=''):   
    return readAllProducts(search)

@app.post("/product")
async def postProduct(productData: Product):
    print(f'producto creado: ', productData)
    return createProduct(productData)
    

@app.delete("/product/{id}")
async def getProducts(id:int):
    return deleteProduct(id) 

@app.post("/cart/{productId}")
async def postCart(productId: int):
    return (f'se agrego el producto cn el id: ', productId)