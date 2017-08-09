FROM alpine:edge

COPY run.sh /root

RUN apk -U add --no-cache mongodb mongodb-tools && \
    rm /usr/bin/mongoperf

VOLUME /data/db

EXPOSE 27017 28017

RUN chmod +x /root/run.sh

ENTRYPOINT [ "/root/run.sh" ]
CMD [ "mongod" ]
