#python
from typing import List
import json
#models
from models.user import User
from models.user_register import UserRegister
from models.tweet import Tweet
#fastapi
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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
def singup(user: UserRegister = Body(...)):
    """
    Sing Up 
    
    This path operations register a user in the app
    
    Parameters:
        - Requets body parameter
            - user: UserRegister
    
    Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
    
    return user
        

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
    summary="shows all users",
    tags=["Users"]
)
def show_all_users():
    """
    Shows All Users
    
    This path operations shows all users in the app
    
    Parameters:
        -

    Returns a json list with all users in the app,
    with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

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
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet
    
    This path operations post a tweet in the app
    
    Parameters:
        - Requets body parameter
            - tweet: Tweet
    
    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        if tweet_dict["updated_at"]:
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
    
    return tweet

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
