FROM alpine:edge

RUN \
apk add --no-cache mongodb && \
rm /usr/bin/mongoperf

VOLUME /data/db
VOLUME /log

COPY run.sh /root
COPY mongod.conf /root

ENTRYPOINT [ "/root/run.sh" ]

CMD [ "mongod", "-f", "/root/mongod.conf" ]