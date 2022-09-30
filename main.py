#python
from typing import List
#models
from models.user import User
from models.tweet import Tweet
#fastapi
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Path Operations

## Users 

### Register a user
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

### Login a user
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

### Show all users
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

### Show a user
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

### Delete a user
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

### Update a user
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

## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
    
)
def home():
    """
    Home
    
    This path operations show all tweets
    """
    return {"Twitter API": "Working!"}

### Post all tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    
)
def post():
    """
    Home
    
    This path operations post a tweet
    """
    return {"Twitter API": "Working!"}

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
    
)
def show_a_tweet():
    """
    Home
    
    This path operations show a tweet
    """
    return {"Twitter API": "Working!"}

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
    
)
def delete_a_tweet():
    """
    Home
    
    This path operations delete a tweet
    """
    return {"Twitter API": "Working!"}

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
    
)
def update_a_tweet():
    """
    Home
    
    This path operations update a tweet
    """
    return {"Twitter API": "Working!"}
