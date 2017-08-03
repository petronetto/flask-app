FROM python:3.6.2-alpine3.6

RUN mkdir /app

COPY . /app

RUN cd /app \
    && pip install -r requeriments.txt --no-cache-dir \
    && mv /app/start.sh /start.sh \
    && chmod +x /start.sh

EXPOSE 5000

WORKDIR /

CMD  [ "/start.sh" ]
