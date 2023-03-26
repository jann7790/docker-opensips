#!/bin/bash

# Set Environment Variables
export DEBIAN_FRONTEND=noninteractive

OPENSIPS_VERSION=3.3
OPENSIPS_BUILD=releases

# Install basic components
apt-get -y update -qq && apt-get -y install gnupg2 ca-certificates mariadb-server sip-tester vim

# Add keyserver, repository
apt-key adv --fetch-keys https://apt.opensips.org/pubkey.gpg
echo "deb https://apt.opensips.org bionic ${OPENSIPS_VERSION}-${OPENSIPS_BUILD}" >/etc/apt/sources.list.d/opensips.list

apt-get -y update -qq && apt-get -y install opensips

OPENSIPS_CLI=true

if [ ${OPENSIPS_CLI} = true ]; then
  echo "deb https://apt.opensips.org bionic cli-nightly" >/etc/apt/sources.list.d/opensips-cli.list
  apt-get -y update -qq && apt-get -y install opensips-cli
fi

if [ -n "${OPENSIPS_EXTRA_MODULES}" ]; then
  apt-get -y install ${OPENSIPS_EXTRA_MODULES}
fi

sed -i "s/log_stderror=no/log_stderror=yes/g" /etc/opensips/opensips.cfg

sed -i "s/RUN_OPENSIPS=no/RUN_OPENSIPS=yes/g" /etc/default/opensips
sed -i "s/DAEMON=\/sbin\/opensips/DAEMON=\/usr\/sbin\/opensips/g" /etc/init.d/opensips

HOST_IP=$(ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7)
sed -i "s/^socket=udp.*5060/socket=udp:${HOST_IP}:5060/g" /etc/opensips/opensips.cfg


# service opensips start
# service mariadb start
