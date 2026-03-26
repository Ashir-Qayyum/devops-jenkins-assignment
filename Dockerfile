FROM python:3.12-slim

WORKDIR /app

# Only copying these two files to the conatiner, there will be no need of .dockerignore it's fine
COPY python-basic-app.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "python-basic-app.py"]

