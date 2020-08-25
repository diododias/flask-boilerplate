FROM python:3.7.7-buster

MAINTAINER Luiz Dias <luiz.dias@altran.com.br>

ENV DEBIAN_FRONTEND=noninteractive
ENV APP_HOME=/app

RUN echo "deb http://nginx.org/packages/mainline/debian/ buster nginx" >> /etc/apt/sources.list
RUN wget https://nginx.org/keys/nginx_signing.key -O - | apt-key add -
RUN apt-get update && apt-get install -y nginx supervisor telnet vim postgresql-devel

COPY requirements.txt $APP_HOME/requirements.txt

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

RUN pip install -U pip && pip install -r $APP_HOME/requirements/dev.txt --upgrade

COPY . $APP_HOME

COPY docker /

WORKDIR $APP_HOME

EXPOSE 80

CMD /usr/bin/supervisord
