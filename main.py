import sys, asyncio
from fastapi import FastAPI,Depends, Path, Response
from fastapi.security import HTTPBasic
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
from database import SessionLocal
from sqlalchemy.orm import Session
import crud,schemas

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
security = HTTPBasic()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#get All customers 
@app.get("/customers", response_model=List[schemas.Customer_test_tab],
        summary="Get All Customers",
        response_description="A List Containing all Customer info")
def get_customers(db: Session = Depends(get_db)):
    res = crud.get_customers(db)

    return res

# get a customer by ID
@app.get("/customers/{ID}", response_model=schemas.Customer_test_tab)
def get_customer_by_ID(ID : int = Path(...,title= "customer id", gt=0),db: Session = Depends(get_db)):
    res =  crud.get_customer_by_ID(db, ID)

    if not res:
        return Response("Customer Not Found", media_type="text/plain",status_code=HTTP_404_NOT_FOUND)

    return res

#Add a customer in db
@app.post("/customers/add/",response_model=schemas.Customer_test_tab)
def create_customer(newCust : schemas.Customer_test_tab, db : Session = Depends(get_db)):
    
    return crud.create_customer(db, newCust)

#delete the customer
@app.delete("/delete/{ID}", )
def delete_customer(ID : int = Path(...,title= "customer id", gt=0), db: Session = Depends(get_db)) -> None:
    existing_cust = crud.get_customer_by_ID(db, ID)

    if existing_cust is not None:
        cust = crud.delete_cust(db, ID)
    
 
#upate customer info
@app.put("/customers/{ID}", response_model=schemas.Customer_test_tab)
def update_customer( cust : schemas.Customer_test_tab, ID : int = Path(...,title= "customer id", gt=0), db: Session = Depends(get_db)):
    return crud.update_customer(db, ID, cust)



