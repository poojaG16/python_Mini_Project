from typing import Optional
from fastapi import Query

from pydantic import BaseModel

from datetime import date



class Customer_test_tab(BaseModel):
    ID : int = Query(..., title= "customer id", gt=0)
    FIRST_NAME : Optional[str] = Query(None, title="Customer first name", max_length=50)
    LAST_NAME : Optional[str] = Query(None, title="Customer last name", max_length=50)
    EMAIL : Optional[str] = Query(None, title="Customer email ID", max_length=100)
    CUSTOMER_TYPE : Optional[str] = Query(None, title="Customer type", max_length=100)
    CREATED_ON : Optional[date] = Query(None, title="Customer entry date")

    class Config:
        orm_mode = True

