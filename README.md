# RESTful-Microservice
Purpose: Run a RESTful microservice with basic CRUD operations and alternate paths on Kubernetes

To build image, make sure Docker is installed and run "_docker image build -t nolanmckenna/rest-app:latest ._"

Then, apply the required YAML files by running "_kubectl apply -f kubernetes_"

Go to http://localhost:31234

To test Fibonacci sequence, add "_/fib?length=NUM_" to the URL, where NUM is the length of the Fibonacci sequence.

To test the Config route, add "_/config_" to the URL.

**Learning Journey:**

When working on this assignment, I first chose what language to work in. I have been exposed to Flask in the past, so decided on Python with Flask. While researching implementations I came across Flask-RESTx, which is designed to easily build REST APIs. It also makes it convenient to integrate SwaggerUI. 

Note: I originally tried to use Flask-RESTPlus, but was getting an import error. This StackOverflow thread introduced me to Flask-RESTx, which worked with no problems (https://stackoverflow.com/questions/60156202/flask-app-wont-launch-importerror-cannot-import-name-cached-property-from-w).

Most of my insight came from the Flask-RESTx documentation (https://flask-restx.readthedocs.io/en/latest/swagger.html).

I also found this article helpful when writing the Dockerfile (https://www.educative.io/answers/how-to-create-a-dockerfile-for-running-a-python-application). Additionally, and as always, the official Docker documentation was also helpful (https://docs.docker.com/engine/reference/builder/). 

Overall, it was nice to rediscover something I have been exposed to/heard about in the past. It was also fun to combine what we have learned about containers and Docker with SwaggerUI and microservices. One thing I appreciate about this assignment was not having to worry about designing and creating a UI. Using Swagger made testing my microservice very easy and convenient. 
