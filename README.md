# RESTful-Microservice
Purpose: Run a RESTful microservice with basic CRUD operations in a container 

To build image, make sure Docker is installed and run "_docker image build -t rest-app ._"  
To run container, run "_docker container run -p 2000:2000 rest-app_"

When working on this assignment, I first chose what language to work in. I have been exposed to Flask in the past, so decided on Python with Flask. While researching the Flask documentation I came across Flask-RESTx, which is designed to easily build REST APIs. It also makes it conveniently integrate SwaggerUI.

Most of my insignt came from the Flask-RESTx documentation (https://flask-restx.readthedocs.io/en/latest/swagger.html).

I also found this article helpful when writing the Dockerfile (https://www.educative.io/answers/how-to-create-a-dockerfile-for-running-a-python-application). Additionally, and as always, the official Docker documentation was also helpful (https://docs.docker.com/engine/reference/builder/). 

Overall, it was nice to rediscover something I have been exposed to/heard about in the past. It was also fun to combine what we have learned about containers and Docker with SwaggerUI and microservices. One thing I appreciate about this assignment was not having to worry about designing and creating a UI. Using Swagger made testing my microservice very easy and convenient. 
