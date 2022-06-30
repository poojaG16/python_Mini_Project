from sqlalchemy import Column, Integer, String, Date

from database import Base

class Customer_test_tab(Base):
    __tablename__ = "customer_test_tab"

    ID = Column(Integer, primary_key=True)
    FIRST_NAME = Column(String(50))
    LAST_NAME = Column(String(50))
    EMAIL = Column(String(100))
    CUSTOMER_TYPE = Column(String(100))
    CREATED_ON = Column(Date)
