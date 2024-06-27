# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t simple-flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 simple-flask-app
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`


# Use the official Python 3.6 image from the Docker Hub
FROM python:3.6

# Set the maintainer label
MAINTAINER veera "veera.narni232@gmail.com"

# Copy the current directory contents into the /app directory in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the entry point to python
ENTRYPOINT ["python"]

# Run app.py when the container launches
CMD ["app.py"]
