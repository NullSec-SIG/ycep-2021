FROM ubuntu
RUN apt-get update
RUN apt-get install -y socat build-essential
RUN apt-get install -y lib32z1

WORKDIR /build
COPY flag.txt /build
COPY bufferman2 /build

RUN chmod +x bufferman2

EXPOSE 12413
CMD ["socat", "TCP4-LISTEN:12413,fork", "EXEC:/build/bufferman2"]