import imp
from config_test import test_app 
from main import app
import crud
import json
import pytest
import schemas

# for getting cust info by ID 
def test_get_customer_by_ID(test_app, monkeypatch):

    #expected output
    test_data = {
        "ID": 110,
        "FIRST_NAME": "Chloe",
        "LAST_NAME": "Martin",
        "EMAIL": "chloe@gmail.com",
        "CUSTOMER_TYPE": "Prime",
        "CREATED_ON": "2022-06-07"
    }

    #patching of function 
    def mock_get(db_session, id):
        return test_data

    #setting attribute using monkeypatch for module scpoe
    monkeypatch.setattr(crud, "get_customer_by_ID", mock_get)

    #get response by calling main module function
    response = test_app.get("/customers/110")
    assert response.status_code == 200
    assert response.json() == test_data


#for all customers
def test_get_customers(test_app, monkeypatch):

    test_data = [
        {
            "ID": 107,
            "FIRST_NAME": "Demo-7",
            "LAST_NAME": "Demo-7",
            "EMAIL": "Demo-1@gmail.com",
            "CUSTOMER_TYPE": "Prime",
            "CREATED_ON": "2022-03-27"
        },
        {
            "ID": 102,
            "FIRST_NAME": "Smith",
            "LAST_NAME": "James",
            "EMAIL": "smithj@gmail.com",
            "CUSTOMER_TYPE": "Regular",
            "CREATED_ON": "2012-06-22"
        },
        {
            "ID": 103,
            "FIRST_NAME": "Williams",
            "LAST_NAME": "Roberta",
            "EMAIL": "william@gmail.com",
            "CUSTOMER_TYPE": "New",
            "CREATED_ON": "2017-11-13"
        },
        {
            "ID": 104,
            "FIRST_NAME": "Franklin",
            "LAST_NAME": "Victoria",
            "EMAIL": "franklin@gmail.com",
            "CUSTOMER_TYPE": "Regular",
            "CREATED_ON": "2016-04-15"
         },
        {
            "ID": 105,
            "FIRST_NAME": "Horton",
            "LAST_NAME": "Michelle",
            "EMAIL": "horton@gmail.com",
            "CUSTOMER_TYPE": "Prime",
            "CREATED_ON": "2018-03-10"
         },
        {
            "ID": 110,
            "FIRST_NAME": "Chloe",
            "LAST_NAME": "Martin",
            "EMAIL": "chloe@gmail.com",
            "CUSTOMER_TYPE": "Prime",
            "CREATED_ON": "2022-06-07"
        }
]

 #patching of function 
    def mock_get(db_session):
        return test_data

    #setting attribute using monkeypatch for module scpoe
    monkeypatch.setattr(crud, "get_customers", mock_get)

    #get response by calling main module function
    response = test_app.get("/customers")
    assert response.status_code == 200
    assert response.json() == test_data


#add customer
def test_create_customer(test_app, monkeypatch):

    test_data = {
        "ID": 111,
        "FIRST_NAME": "Rose",
        "LAST_NAME": "Richard",
        "EMAIL": "rose@gmail.com",
        "CUSTOMER_TYPE": "Prime",
        "CREATED_ON": "2012-01-01"
    }

    #patching of function 
    def mock_post(db_session, payload):
        return test_data

    #setting attribute using monkeypatch for module scpoe
    monkeypatch.setattr(crud, "create_customer", mock_post)

    #get response by calling main module function
    response = test_app.post("/customers/add/", data=json.dumps(test_data))
    assert response.status_code == 200
    assert response.json() == test_data


# for getting cust info by ID 
def test_delete_customer(test_app, monkeypatch):
    #patching of function 
    def mock_delete(db_session, id):
       pass

    def mock_get(db_session, id):
        pass

    #setting attribute using monkeypatch for module scpoe
    monkeypatch.setattr(crud, "delete_cust", mock_delete)
    monkeypatch.setattr(crud, "get_customer_by_ID", mock_get)
    #get response by calling main module function
    response = test_app.delete("/delete/110")
    assert response.status_code == 200


def test_update_customer(test_app, monkeypatch):

    #expected output
    test_data = {
        "ID": 110,
        "FIRST_NAME": "Chloe",
        "LAST_NAME": "Martin",
        "EMAIL": "chloe@gmail.com",
        "CUSTOMER_TYPE": "New",
        "CREATED_ON": "2022-02-17"
    }

    #patching of function 
    def mock_put(db_session, ID, payload):
        return test_data

    #setting attribute using monkeypatch for module scpoe
    monkeypatch.setattr(crud, "update_customer", mock_put)

    #get response by calling main module function
    response = test_app.put("/customers/110", data=json.dumps(test_data))
    assert response.status_code == 200
    assert response.json() == test_data
