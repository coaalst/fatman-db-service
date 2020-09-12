from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app-deploy
COPY . /app-deploy

RUN pip3 --no-cache install -r requirements.txt

EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]


