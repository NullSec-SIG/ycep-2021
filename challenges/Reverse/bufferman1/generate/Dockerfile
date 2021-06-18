FROM ubuntu
RUN apt-get update
RUN apt-get install -y socat build-essential
RUN apt-get install -y lib32z1

WORKDIR /build
COPY flag.txt /build
COPY bufferman1 /build

RUN chmod +x bufferman1

EXPOSE 12412
CMD ["socat", "TCP4-LISTEN:12412,fork", "EXEC:/build/bufferman1"]