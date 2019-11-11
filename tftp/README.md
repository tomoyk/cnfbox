# tftp

Build

```
docker build -t tftp .
```

Run

```
docker run -it -p 69:69 tftp
```

Debug

```
echo "get /var/tftpboot/hello.txt" | tftp 127.0.0.1
```
