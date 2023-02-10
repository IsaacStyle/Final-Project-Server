0.) `pip install -r requirements.txt` install all dependnecies in requirements.txt

1.) `mkvirtualenv ga` / ` workon reameme`

2.) `django-admin startproject ga .`

3.) `pip install django`

4.) `pip freeze > requirements.txt`

5.)  `touch create-database.sql ` and add:

    CREATE DATABASE readme;

    CREATE USER server_admin WITH PASSWORD '1234'

    GRANT ALL PRIVILEDGES ON DATABASE ga TO ga_admin;



6.) `psq -f create-database.sql ` To create sq database from the command line 

7.) 

--- 

### Back-end:
Models:
- Post 
- User 
- Subreddit
- Comments

Post(BaseModel):
    title = CharField(max_length = 250)
    text = TextField()
    img_url = TextField()
    up_vote = IntField()
    down_vote = IntField()
    user_id = IntField()
    sub_reddit_id = IntField()
    *** maybe *** date = Datetime()
--- 
User(BaseModel):
    user_name = CharField(max_length = 20)
    sub_reddits = ArrayField()
    comments = ArrayField()
    profile_pic = TextField()
---
Subs(BaseModel):
    title = CharField(max_length = 20)
    followers = ArrayField()
    creator = CharField(max_length = 20)
    post_id = ArrayField()
    descript = TextField()
    *** maybe *** date = Datetime()
--- 

Comments(BaseModel):
    comment =  TextField()
    user_id = CharField(max_length = 20)
    post_id = CharField(max_length = 20)
    sub_id = CharField(max_length = 20)
    up_vote = IntField()
    down_vote = IntField()
    ß