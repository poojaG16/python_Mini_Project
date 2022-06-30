
from fastapi import HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
import models,schemas


def get_customers(db: Session):
    return db.query(models.Customer_test_tab).all()

def get_customer_by_ID(db: Session, id : int):
    cust = db.query(models.Customer_test_tab).filter(models.Customer_test_tab.ID==id).first()

    if not cust:
        raise HTTPException(status_code=404, detail="No Such Customer Present!")
    
    return cust

# def add_customer(db: Session):
def create_customer(db: Session, cust : schemas.Customer_test_tab):
    new_cust = models.Customer_test_tab(ID = cust.ID, FIRST_NAME = cust.FIRST_NAME, LAST_NAME = cust.LAST_NAME, EMAIL = cust.EMAIL, CUSTOMER_TYPE = cust.CUSTOMER_TYPE, CREATED_ON = cust.CREATED_ON)
    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)
    return new_cust
   
def delete_cust(db: Session, id : int):
    cust = db.query(models.Customer_test_tab).filter(models.Customer_test_tab.ID==id).first()
    db.delete(cust)
    db.commit()
    return cust

def update_customer(db : Session, id: int, newCust : schemas.Customer_test_tab):
    #find the custmoer
    ext_cust = get_customer_by_ID(db, id)

    #if its not present raise an exception
    if not ext_cust:
       
        raise HTTPException(status_code=404, detail="No Such Customer Present!")
    
    #found : update values
    else:
        ext_cust.FIRST_NAME = newCust.FIRST_NAME
        ext_cust.LAST_NAME = newCust.LAST_NAME
        ext_cust.EMAIL = newCust.EMAIL
        ext_cust.CUSTOMER_TYPE = newCust.CUSTOMER_TYPE
        ext_cust.CREATED_ON = newCust.CREATED_ON
        db.commit()
        return ext_cust



    

