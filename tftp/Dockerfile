FROM alpine:3.10
WORKDIR /work
EXPOSE 69
RUN apk --no-cache add tftp-hpa
RUN echo "hello" > /var/tftpboot/hello.txt
ENTRYPOINT ["/usr/sbin/in.tftpd", "-4", "-v", "-l","-L", "-c", "-a"]
CMD ["0.0.0.0"]
