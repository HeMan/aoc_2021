FROM alpine:latest
RUN apk add micropython --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
WORKDIR /src
COPY ./ .
CMD /src/aoc.sh
