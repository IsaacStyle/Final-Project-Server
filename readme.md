## Final-Project-Server
##### This is the Backend of a Fullstack Social Media application built using Django, Postgresql and deployed with Railway.

Members:
- Angela Kwon
- Xavier Valtierra
- Jack Jiang
- Zack Lay
- Justin Ozkan 
- Gabe Cohen
- Edward Olstrom


### TO START Part I

- 1.) `git clone <repo>` DO NOT FORK
- 2.) Run `git branch -a` to view remote branches(your name should not be here - yet) and see which branch you are on. (There is a * next to the branch)
- 3.) Run `git checkout -b <thenameofyourbranch>` to make a remote branch.


### Part II
    AFTER CHANGES HAVE BEEN LOCALLY

- 1.) `git add .`
- 2.) `git commit -m 'a message that makes sense'`
- 3.) *** This is important ***  `git push origin <thenameofyourbranch>`
- 4.) Go onto github and create a pull request. Please add comments on what the code does /  updates you have made.


### Part III
    AFTER CHANGES HAVE BEEN MERGED WITH DEV BRANCH 

- 1.) Please DO NOT pull changes ONTO your old code i.e the branch you just pushed and that got merged.  
- 2.) PLEASE DO THE FOLLOWING: `git checkout -b <NEWthenameofyourNEWbranch> `

*** NOTE: Create a new branch your old branch is no longer needed and will create confilcts if you try to pull onto it ***

- 3.) Next, run: `git pull origin dev`  

- 4.) Your branch should be up to date with the dev

## Technologies Used
#### Django
  A powerful Python framework built for the purpose of web development. Its popular for its ease of use, due to is accessible interface and built in Authentication.
#### Postgresql
  A intuitive relational database which is used to store the social media data that users post to the site.
#### Railway
  A deployment tool, which comes with its own Postgresql cloud built in, so you can access the Server data with less complications.
#### Django Rest Framework
  Django middleware which defines your URL end points, abstracts much of the CRUD (Create, Read, Edit and Delete Functionality) from the coding process, as well as responsible for helping create a restful application.
#### Psycopg2 Binary
  Another Django middleware which eases the ability for Django to interact with your Postgresql Database.
#### Django Environ
  Allows you to interact with environment variables within your Django application, allowing you to protect your sensitive data from Nefarious Fiends.
#### Django Cors Headers
  Handles the server headers required specifically for Cross-Origin Resource Sharing (CORS). A lack of this makes it difficult to interact with the Database.
#### Gunicorn
  A WSGI server application for Django, which abstracts much of the logic for your deployed applications.
#### WhiteNoise
  Django middleware which compresses your files, hashes them with unique indentifiers so they can be safely cached. Useful for dealng with staaticc files.

## Project Schemas
##### This project employs 4 basic Schemas: Posts, Comments, Users, and Sub-Pages

#### Posts contain:
    title - A Char Field which denotes the title.
    text - A Text Field to determine the text content of the post if it is desired.
    img_url - A Text Field to determine the image if one is used.
    up_votes - An Integer Field which stores the positive interaction from Users.
    down_votes - An Integer Field which stores the negative interaction from Users.
    user - Connects the post to a User in the database.
    sub - Connects the pst to a Sub Page in he database.
#### Comments contain:
    comment - A Text Field to determine the text content of the comment.
    up_votes - An Integer Field which stores the positive interaction from Users.
    down_votes - An Integer Field which stores the negative interaction from Users.
    commenter - Connects the post to a User in the database.
    post- Connects the comment to a post in the database.
#### Subs contain:
    title - A Char Field which denotes the title.
    followers - An Integer Array which contains the id's of the following Users.
    creator - Connects the post to a User in the database.
    description - A Text Field which contains a description of the Sub Page
    * img - A Text Field which contains the Url of the Sub Page profile image.
    * cover_img - A Text Field which contains the Url of the cover image of the Sub Page
##### All fields contain CRUD functionaliy for all requests (Get, Post, Put, Delete)
  
