#!/bin/bash

sed -i "s/RUN_OPENSIPS=no/RUN_OPENSIPS=yes/g" /etc/default/opensips
sed -i "s/DAEMON=\/sbin\/opensips/DAEMON=\/usr\/sbin\/opensips/g" /etc/init.d/opensips

DOCKER_IP=$(ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7)
# HOST_IP=$1
echo "host ip ${HOST_IP}"

service mariadb start
mysql <  createDBUser.sql
printf '\n'| opensips-cli -x database create
printf ${HOST_IP}'\n'|opensips-cli -x user add 1000 123456;



sed -i "s/^socket=udp.*5060/socket=udp:${DOCKER_IP}:5060\nadvertised_address=${HOST_IP}/g" /etc/opensips/opensips.cfg

cat /etc/opensips/opensips.cfg|grep socket
cat /etc/opensips/opensips.cfg|grep advertised_address


# skip syslog and run opensips at stderr
/usr/sbin/opensips -FE