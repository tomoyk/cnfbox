FROM alpine:3.10
WORKDIR /work
EXPOSE 67
RUN apk --no-cache add dhcp
RUN touch /var/lib/dhcp/dhcpd.leases
ADD dhcpd.conf /etc/dhcp/dhcpd.conf
CMD ["/usr/sbin/dhcpd", "-4", "-f", "-cf", "/etc/dhcp/dhcpd.conf"]
