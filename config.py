from hashlib import new
from logging import exception, warning
import pytube
import tldextract
import os
import telebot
import re
import requests
from bs4 import BeautifulSoup
import time
import shutil
from os import listdir
from os.path import isfile, join
import string
import numpy as np

#re.search(r"\b" + re.escape(string1) + r"\b", string2)


def find_cm_title(title):
    cwd = os.getcwd()
    onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
    res = [i for i in onlyfiles if title in i]
    return res[0]


video_title = "How do websites work?"
video_title = video_title.rstrip(string.punctuation)
var = find_cm_title(video_title)
print(var)

print(np.array(range(-1, 10)))
