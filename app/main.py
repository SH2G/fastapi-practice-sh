# app/main.py
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, repositories, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI 연습해보자",
    description="간단한 상품 조회, 등록, 삭제, 업데이트 API 제공",
    version="0.1"
)

# 상품 목록 조회
@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = repositories.get_products(db, skip=skip, limit=limit)
    return products

# 새로운 상품 등록
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return repositories.create_product(db=db, product=product)

# 상품 삭제
@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_deleted = repositories.delete_product(db, product_id=product_id)
    if not product_deleted:
        raise HTTPException(status_code=404, detail="상품 없음")
    return {}

# 상품 업데이트
@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated_product = repositories.update_product(db, product_id=product_id, product=product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="상품 없음")
    return updated_product
