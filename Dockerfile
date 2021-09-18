FROM python:3.6.8-slim

LABEL maintainer="errakho mohammed <mohammederrakho807@gmail.com>"

# App setup
COPY . /youtupe-bot
WORKDIR /youtupe-bot
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt .


CMD ["python", "telegram_bot_youtupe.py"]