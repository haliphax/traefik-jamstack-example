# Demo Web API container image
FROM python:3.8-alpine
LABEL author="haliphax"
EXPOSE 5000
VOLUME /app
CMD [ "python", "-m", "demo" ]
WORKDIR /app
ADD ./webapi/ /app/
RUN pip install -e /app
