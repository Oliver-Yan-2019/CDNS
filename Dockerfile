FROM wfarn86/python2_requests


ADD . /cdns_server
WORKDIR /cdns_server
VOLUME ["/var/data"]

ARG HCM_VERSION
ENV HCM_VERSION=$HCM_VERSION

ENV CDNS_AUTH='yanzihuan'

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && \
    chmod +x /cdns_server/start.sh

CMD cd /cdns_server && sh /cdns_server/start.sh

EXPOSE 8000
