FROM python:3.6-alpine

RUN adduser -D hack

WORKDIR /home/hack
COPY requirements.txt requirements.txt
COPY app app
COPY migrations migrations
COPY main.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP main.py

RUN chown -R hack:hack ./
USER hack

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]