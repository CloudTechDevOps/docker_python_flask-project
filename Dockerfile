FROM python:3.6
MAINTAINER veera "veera.narni232@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["python", "app.py"]
