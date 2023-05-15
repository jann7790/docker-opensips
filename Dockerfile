FROM debian:bullseye
LABEL maintainer="Razvan Crainea <razvan@opensips.org>"

USER root

# Set Environment Variables
ENV DEBIAN_FRONTEND noninteractive

ARG OPENSIPS_VERSION=3.3
ARG OPENSIPS_BUILD=releases

#install basic components
RUN apt-get -y update -qq && apt-get -y install gnupg2 ca-certificates mariadb-server

#backend for linphone
RUN apt-get -y update -qq && apt-get -y install python3 python3-pip && pip3 install mysql-connector-python



#for testing
RUN apt-get -y update -qq && apt-get -y install vim

#add keyserver, repository
RUN apt-key adv --fetch-keys https://apt.opensips.org/pubkey.gpg
RUN echo "deb https://apt.opensips.org bullseye ${OPENSIPS_VERSION}-${OPENSIPS_BUILD}" >/etc/apt/sources.list.d/opensips.list

RUN apt-get -y update -qq && apt-get -y install opensips

ARG OPENSIPS_CLI=false
RUN if [ ${OPENSIPS_CLI} = true ]; then \
    echo "deb https://apt.opensips.org bullseye cli-nightly" >/etc/apt/sources.list.d/opensips-cli.list \
    && apt-get -y update -qq && apt-get -y install opensips-cli \
    ;fi

ARG OPENSIPS_EXTRA_MODULES
RUN if [ -n "${OPENSIPS_EXTRA_MODULES}" ]; then \
    apt-get -y install ${OPENSIPS_EXTRA_MODULES} \
    ;fi

RUN rm -rf /var/lib/apt/lists/*
RUN sed -i "s/log_stderror=no/log_stderror=yes/g" /etc/opensips/opensips.cfg

COPY run.sh /run.sh
COPY backend.py /backend.py
RUN chmod +x /run.sh


ENTRYPOINT ["./run.sh"]
# ENTRYPOINT ["/usr/sbin/opensips", "-FE"]