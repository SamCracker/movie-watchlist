FROM alpine:latest

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev
RUN pip install --upgarde pip

WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install
RUN pipenv shell

CMD ["python3", "app.py"]