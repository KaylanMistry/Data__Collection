FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

ENV SLACK_BOT_TOKEN=BOT_TOKEN
ENV SLACK_APP_TOKEN=APP_TOKEN

CMD [ "python", "app.py" ]