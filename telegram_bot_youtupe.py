from logging import exception, warning
import pytube
import tldextract
import os
import telebot
import re
from os import listdir
from os.path import isfile, join
import string
import numpy as np
from s3_module import *


def get_bot(credentials):
    """get the telegram bot object.
    """
    with open(credentials) as f:
        API_KEY = f.readlines()[0].split("=")[1]
    bot = telebot.TeleBot(API_KEY)

    return bot


bot = get_bot('credentils.txt')


def find_cm_title(title):
    """get complete video title from root directory
    """
    cwd = os.getcwd()
    onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
    res = [i for i in onlyfiles if title in i]
    return res[0]


def find_url(text):
    """extract the target url from text.
    Parameters
    ----------
    text : str
        String from which url to be extracted.
    Returns
    -------
    Optional[str]
        Return url if present in the given string.
    """

    return re.findall(
        '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', str(text))


def download_video(message, video_url):
    """download youtupe video given it's url.
    """
    youtube = pytube.YouTube(str(video_url))
    try:
        if tldextract.extract(str(video_url)).domain != "youtu":
            video = youtube.streams.first()
            video.download()
        else:
            warning = "Not a valid youtupe url"
            print(warning)

        video_title = youtube.title
        video_title = video_title.rstrip(string.punctuation)
        print(video_title)
        video_title_cm = find_cm_title(video_title)
        # video_title_cm.find(video_title):
        #list_number = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        bot.send_chat_action(message.chat.id, "typing")

        try:
            if video_title_cm.find(video_title) in list(range(-1, 10)):
                with open(str(video_title_cm), "rb") as vd:
                    bot.send_video(message.chat.id, vd)

        except Exception as e:
            raise e

    except Exception as e:
        raise e

    return True


@bot.message_handler(commands=["download"])
def get_s3_cached_videos(message):

    bot.send_chat_action(message.chat.id, "typing")
    objects = list_s3_files(
        "landingzone1999c7acde43-8029-49ce-b848-153513fd51c6")
    file_names = ' '.join(object)
    bot.send_message(message, file_names)


@bot.message_handler(func=lambda m: True)
def dowload_video(message):
    # with open("video1.mp4", 'rb') as fn:
    url = find_url(message)

    if str(url[0]).endswith(".jpg"):
        bot.send_photo(
            message.chat.id, url[0])
    else:
        download_video(message, url)


bot.polling()
