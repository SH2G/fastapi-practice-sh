from sqlalchemy.orm import Session
from . import models, schemas

# 상품 목록 조회
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

# 상품 등록
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name, 
        description=product.description, 
        price=product.price, 
        stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 상품 삭제
def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False

# 상품 업데이트
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.stock = product.stock
        db.commit()
        db.refresh(db_product)
        return db_product
    return None
