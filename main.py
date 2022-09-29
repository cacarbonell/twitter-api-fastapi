#models
from models.user import User
from typing import List
#fastapi
from fastapi import FastAPI
from fastapi import status

app = FastAPI()


@app.get(path="/")
def home():
    """
    Home
    
    This is point start the app
    """
    return {"Twitter API": "Working!"}

# Users 

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def singup():
    """
    Sing Up
    
    This path operations register a user
    """
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    """
    Sing Up
    
    This path operations login a user
    """
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="show all users",
    tags=["Users"]
)
def show_all_users():
    """
    Sing Up
    
    This path operations show all user
    """
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["Users"]
)
def show_a_user():
    """
    Sing Up
    
    This path operations show a user
    """
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user():
    """
    Sing Up
    
    This path operations delete a user
    """
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_a_user():
    """
    Sing Up
    
    This path operations update a user
    """
    pass


