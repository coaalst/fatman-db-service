FROM python:latest

WORKDIR /app-deploy
COPY . /app-deploy

RUN pip --no-cache install -r requirements.txt

EXPOSE 5001
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]


